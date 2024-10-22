
# lab 4
# Process Implementation: This class implements the Process interface. It maintains:
# Name: Jatin K rai
#DawID

"""
Process Implementation: This class implements the Process interface. It maintains:
• A local vector clock (using a VectorClock class, explained later).
• A boolean flag indicating critical section access status.
• A reference to a shared MaekawaManager object (explained later).
• The quorum set for this process (obtained from getQuorum or pre-configured).
• It implements methods from the interface:
o requestCriticalSection(): Increments the local clock, sends REQUEST messages with the current clock to all processes in its quorum using RMI.
o releaseCriticalSection(): Sets the critical section flag to false, sends RELEASE messages to all processes using RMI.
o getQuorum (optional): Returns the pre-configured quorum set.

"""



import Pyro5.api
from iLab4MaekawaMutualExclusion import iLab4MaekawaMutualExclusion
from clsLab4VectorClock import clsLab4VectorClock


# implement class witn instance_mode single.
# pyro objects for instance_mode=single (singletons, just one per daemon)

#@Pyro5.api.behavior(instance_mode="single")

@Pyro5.api.expose
# Class representation
class clsLab4MaekawaMutualExclusionP0(iLab4MaekawaMutualExclusion):

     #static request send  for 3 process using Quorum.
    P0RequetSendQueue = []
    P1RequetSendQueue = []
    P2RequetSendQueue = []

    #receive Queue for 3 process using Quorum.
    P0recevieQueue = []
    P1recevieQueue = []
    P2recevieQueue = []

    #static Quorum for 3 process using Quorum.
    QuoromforP0 = []
    QuoromforP1 = []
    QuoromforP2 = []


    #processaarry for 3 process using Quorum.
    processarray = []

    # constructor
    def __init__(self, maekawa_manager, number_of_process):
        self.vector_clock = clsLab4VectorClock()
        self.process_id = 0 #hard coded
        self.quorum = [1] #hard coded
        self.in_critical_section = False
        self.numberofprocess = number_of_process;
        #o Remote objects for Process and MaekawaManager (if used).
        self.objmaekawa_manager = Pyro5.api.Proxy(maekawa_manager)
        self.SetupQuorum()
        self.SetupSendandReceiveQueue()

 #Set the pre_defined_configuration
    def SetupQuorum(self):
        try:
            #check for number of process
            if (self.numberofprocess <= 0):
               self.numberofprocess = 3  

            if (self.numberofprocess > 0):
                # Create dynamic process array.
               
                for index in range (0, self.numberofprocess):
                    self.processarray.append("P" + str(index))
            #let us set the quorum for process
            # for P0 the quorum will be (1,2)
            # for P1 the quorum will be (0.2)
            # for P2 the quorum will be (0,1)
            self.QuoromforP0 = [1,2]
            self.QuoromforP1 = [0,2]
            self.QuoromforP2 = [0,1]

        except Exception as error:
            print("clsLab4MaekawaMutualExclusion.SetupQuorum(): Process failed.")
            print (error)
        finally:
            print("clsLab4MaekawaMutualExclusion.SetupQuorum(): Process completed successfully.")


   #this is for reset the Queue
    def SetupSendandReceiveQueue(self):
        try:
            #check for number of process
            if (self.numberofprocess <= 0):
               self.numberofprocess = 3  

            if (self.numberofprocess > 0):
                # Create Queue for send and received.
                # there are three send queue
                # there three recevie Queue


                #placeholders for all process queues.
                self.P0RequetSendQueue = []
                self.P1RequetSendQueue = []
                self.P2RequetSendQueue = []

                self.P0recevieQueue = []
                self.P1recevieQueue = []
                self.P2recevieQueue = []

        except Exception as error:
            print("clsLab4MaekawaMutualExclusion.SetupSendandReceiveQueue(): Process failed.")
            print (error)
        finally:
            print("clsLab4MaekawaMutualExclusion.SetupSendandReceiveQueue(): Process completed successfully.")

    
    #requestCriticalSection(): Increments the local clock, sends REQUEST messages with the current 
    # clock to all processes in its quorum using RMI.
    def requestCriticalSection(self, processidrequestforCS):
        try:
            self.process_id =  processidrequestforCS
            self.vector_clock.increment(self.process_id)

            print ("requestCriticalSection : vector_clock value = " , self.vector_clock.get_time(self.process_id))
            print ("requestCriticalSection : process id value = " , self.process_id)

            #Request message to quorom process for critical section for requested process.
            request_message = {
                'type': 'REQUEST',
                'process_id': self.process_id,
                'clock': self.vector_clock.get_time(self.process_id)
            }

            #get the qurom of this process id.
            self.quorum = self.getQuorum(processidrequestforCS)

            # broadcast request message to all quorum process for this requested process
            for pid in self.quorum:
                self.receiveMessage(request_message, pid) # request message.

            #reply and provide permission from quorom process to sender
            for pid in self.quorum:
                self.replyforCriticalSection(pid)  # reply from pid to sender process

            #Check for all permissions then allow for enter into critical section.
            bpermissiongranredbyquorom = False
            for pid in self.quorum:
                RequetsendQueue = []
                ReceiveQueue = []
                
                print ("requestCriticalSection : checking for Request send Queue for process id value = " , pid)
                if (pid == 0):
                    RequetsendQueue= self.P0RequetSendQueue
                elif (pid == 1):
                  RequetsendQueue= self.P1RequetSendQueue
                elif (pid == 2):
                   RequetsendQueue= self.P2RequetSendQueue
                else:
                   RequetsendQueue= self.P0RequetSendQueue
                
                print ("requestCriticalSection : checking for Receive Queue for process id value = " , pid)
                # send message to the sender process id.
                if (pid == 0):
                    ReceiveQueue = self.P0recevieQueue
                elif (pid == 1):
                    ReceiveQueue = self.P1recevieQueue
                elif (pid == 2):
                    ReceiveQueue = self.P2recevieQueue
                else:
                   ReceiveQueue =  self.P0recevieQueue

                #for Qurorom receive Queue if empty and Request Send Queue is greater than 0 then it is good to allow permission
                if ((len(ReceiveQueue)) == 0) and ((len(RequetsendQueue)) > 0):
                    print ("requestCriticalSection : checked for Receive Queue is zero and send Queue is more than one for process id value = " , pid)
                    bpermissiongranredbyquorom = True
                else:
                    print ("requestCriticalSection : checked for Receive Queue is not zero and send Queue is not more than one for process id value = " , pid)
                    bpermissiongranredbyquorom = True

            # Allow for crtical sections        
            if (bpermissiongranredbyquorom == True):
                    print ("requestCriticalSection : Entered into the Critical section for this process id = " , self.process_id)
                    bpermissiongranredbyquorom = True
                    self.process_id = processidrequestforCS

                    isGranted = self.objmaekawa_manager.grantEntry(self.process_id, self.vector_clock.get_time(self.process_id))

                    if(isGranted == True):
                        print ("requestCriticalSection : self.in_critical_section allowed")
                    else:
                        print ("requestCriticalSection : self.in_critical_section does not allowed")
            else:
                    print ("requestCriticalSection : self.in_critical_section does not allowed for this process id = ", self.process_id)

            print ("requestCriticalSection : self.in_critical_section value is True")
        except Exception as error:
            print("clsLab4MaekawaMutualExclusion.requestCriticalSection(): Process failed.")
            print (error)
        finally:
            print("clsLab4MaekawaMutualExclusion.requestCriticalSection(): Process completed successfully.")
        
        
    #releaseCriticalSection(): Sets the critical section flag to false, sends RELEASE messages to all processes using RMI.
    def releaseCriticalSection(self, processidreleasefromCS):

        try:
            self.process_id =  processidreleasefromCS
            print ("releaseCriticalSection : vector_clock value = " , self.vector_clock.get_time(self.process_id))
            print ("releaseCriticalSection : process id value = " , self.process_id)
            self.in_critical_section = False
            print ("releaseCriticalSection : self.in_critical_section value is False")

            #reply for release from quorom 
            for pid in self.quorum:
                self.replyforCriticalSection(pid)  # reply from pid to sender process
            
            
            release_message = {
                'type': 'RELEASE',
                'process_id': self.process_id
            }


             #get the qurom of this process id.
            self.quorum = self.getQuorum(processidreleasefromCS)
            for pid in self.quorum:
                self.receiveMessage(release_message, pid)  # to test dummy.

            

        except Exception as error:
            print("clsLab4MaekawaMutualExclusion.releaseCriticalSection(): Process failed.")
            print (error)
        finally:
            print("clsLab4MaekawaMutualExclusion.releaseCriticalSection(): Process completed successfully.")

    #replyforCriticalSection(): reply for the process who requested for critical section, sends REPLY messages to sender processes.
    def replyforCriticalSection(self, processidreleasefromCS):

        try:
            self.process_id =  processidreleasefromCS
            print ("replyforCriticalSection : vector_clock value = " , self.vector_clock.get_time(self.process_id))
            print ("replyforCriticalSection : process id value = " , self.process_id)
            self.in_critical_section = False
            print ("replyforCriticalSection : self.in_critical_section value is False")
            reply_message = {
                'type': 'REPLY',
                'process_id': self.process_id
            }
            #reply from pid to current process sender id
            self.receiveMessage(reply_message, processidreleasefromCS)  # to test dummy.

            #get the qurom of this process id.
            # self.quorum = self.getQuorum(processidreleasefromCS)

            #for pid in self.quorum:
             #   self.receiveMessage(reply_message, pid)  # to test dummy.
        except Exception as error:
            print("clsLab4MaekawaMutualExclusion.replyforCriticalSection(): Process failed.")
            print (error)
        finally:
            print("clsLab4MaekawaMutualExclusion.replyforCriticalSection(): Process completed successfully.")
        
    #Returns the pre-configured quorum set.
    def getQuorum(self, qprocessid):
        retunrnval = []
        try:
            if (qprocessid < 0):
                qprocessid = 0  

            if (qprocessid == 0):
                retunrnval =  self.QuoromforP0 
            elif (qprocessid == 1):
                retunrnval =  self.QuoromforP1
            elif (qprocessid == 2):
                retunrnval =  self.QuoromforP2
            else:
                retunrnval =  self.QuoromforP0  # default Process 0
        except Exception as error:
            print("clsLab4MaekawaMutualExclusion.getQuorum(): Process failed.")
            print (error)
        finally:
            print("clsLab4MaekawaMutualExclusion.getQuorum(): Process completed successfully.")

        return retunrnval
    
    # expose receive message.
    def receiveMessage(self, message, rprocessid):
        try:

            if (rprocessid < 0):
                rprocessid = 0  

            if message['type'] == 'REQUEST':
                # Handle REQUEST message
                try:
                    if (rprocessid == 0):
                        self.P0RequetSendQueue.append(str(message['process_id']) + "0")
                    elif (rprocessid == 1):
                        self.P1RequetSendQueue.append(str(message['process_id']) + "1")
                    elif (rprocessid == 2):
                        self.P2RequetSendQueue.append(str(message['process_id']) + "2")
                    else:
                        self.P0RequetSendQueue.append(str(message['process_id']) + "0")
                except Exception as error:
                    print("clsLab4MaekawaMutualExclusion.receiveMessage().append() : Process failed.")
                    print (error)
                finally:
                    print("clsLab4MaekawaMutualExclusion.receiveMessage().append() : Process completed successfully.")
            elif message['type'] == 'RELEASE':
                # Handle RELEASE message
                try:
                  
                    if ((rprocessid == 0) and (len(self.P0recevieQueue) > 0)):
                        self.P0recevieQueue.pop(0) #remove from top.
                    elif ((rprocessid == 1) and (len(self.P1recevieQueue) > 0)):
                        self.P1recevieQueue.pop(0)
                    elif((rprocessid == 2) and (len(self.P2recevieQueue) > 0)):
                        self.P2recevieQueue.pop(0)
                    else:
                        print("clsLab4MaekawaMutualExclusion.receiveMessage().pop(0) : Else part of Reply  self.P0recevieQueue.pop(0) #remove from top.")
                        
                except Exception as error:
                    print("clsLab4MaekawaMutualExclusion.receiveMessage().pop(0) : Process failed.")
                    print (error)
                finally:
                    print("clsLab4MaekawaMutualExclusion.receiveMessage().pop(0) : Process completed successfully.")
            elif message['type'] == "REPLY":
                # Handle REPLY message
                try:
                    # send message to the sender process id.
                    sprocessid = int(message['process_id'])
                    if (sprocessid == 0):
                        self.P0RequetSendQueue.append(str(rprocessid) + "0")
                    elif (sprocessid == 1):
                        self.P1RequetSendQueue.append(str(rprocessid) + "1")
                    elif (sprocessid == 2):
                        self.P2RequetSendQueue.append(str(rprocessid) + "2")
                    else:
                        self.P0RequetSendQueue.append(str(rprocessid) + "0")
                    #remove from own pid  of Quorom
                    if ((rprocessid == 0) and (len(self.P0RequetSendQueue) > 0)):
                        self.P0RequetSendQueue.pop(0) #remove from top.
                    elif ((rprocessid == 1) and (len(self.P1RequetSendQueue) > 0)):
                        self.P1RequetSendQueue.pop(0) #remove from top.
                    elif ((rprocessid == 2) and (len(self.P2RequetSendQueue) > 0)):
                        self.P2RequetSendQueue.pop(0) #remove from top.
                    else:
                        print("clsLab4MaekawaMutualExclusion.receiveMessage().pop(0) : Else part of Reply  self.P0RequetSendQueue.pop(0) #remove from top.")
                       # self.P0RequetSendQueue.pop(0) #remove from top.
                    
                except Exception as error:
                    print("clsLab4MaekawaMutualExclusion.receiveMessage().reply() : Process failed.")
                    print (error)
                finally:
                    print("clsLab4MaekawaMutualExclusion.receiveMessage().reply() : Process completed successfully.")

        except Exception as error:
            print("clsLab4MaekawaMutualExclusion.receiveMessage(): Process failed.")
            print (error)
        finally:
            print("clsLab4MaekawaMutualExclusion.receiveMessage(): Process completed successfully.")