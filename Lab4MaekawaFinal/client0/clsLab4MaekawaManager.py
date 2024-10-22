
# lab 4
# MaekawaManager Implementation (Optional): This class implements the MaekawaManager interface. 
# Name: Jatin K rai
#DawID

"""
# MaekawaManager Implementation (Optional): This class implements the MaekawaManager interface. It maintains:
• A queue for holding received REQUEST messages.
• It implements methods from the interface:
o grantEntry(processId, clock):
 Updates the queue with the received request.
 Checks if the requesting process has received permission (votes) from a sufficient number of processes in its chosen quorum based on received messages.
 If enough votes are received, grants permission to the requesting process by sending a GRANT message to all processes using RMI.


"""
import Pyro5.api
from iLab4MaekawaManager import iLab4MaekawaManager

# implement class witn instance_mode single.
# pyro objects for instance_mode=single (singletons, just one per daemon)

#@Pyro5.api.behavior(instance_mode="single")

@Pyro5.api.expose
# Class representation
class clsLab4MaekawaManager(iLab4MaekawaManager):
    def __init__(self):
        self.request_queue = []
        self.current_process = None
    """
    Develop the interfaces and classes mentioned above.
    Implement RMI functionalities:
    • Use UnicastRemoteObject to create remote objects for Process and MaekawaManager (if used).
    • Use the Naming class to register these remote objects on the RMI registry.
    3. Process Logic:
    • Each process creates its own Process object and references a shared MaekawaManager object (if used) or directly communicates with other processes.
    • A process calls requestCriticalSection to enter the critical section. This triggers sending REQUEST messages with the current vector clock to all processes in its pre-defined quorum using RMI.
    • Processes receiving a REQUEST message update their local state and might send a GRANT message to the requesting process if it meets the quorum requirement (based on Maekawa's algorithm).
    • The MaekawaManager (if used) can act as a central coordinator, tracking requests and sending GRANT messages when appropriate.
    • Upon receiving a GRANT message from a sufficient number of processes in its quorum, the requesting process can enter the critical section.
    • After exiting the critical section, the process calls releaseCriticalSection which sends RELEASE messages to all processes using RMI.
    """
    # expose grantEntry
    @Pyro5.api.expose
    def grantEntry(self, process_id, clock):

        bGrant = False
        try: 
            print ("clsLab4MaekawaManager:grantEntry process_id = " , process_id)
           
           #Grant entry method called once vote will be provided.
            self.request_queue.append((process_id, clock))
            # Logic to check if the process has enough votes
            # If enough votes, send GRANT message
            #self.request_queue.sort(key=lambda x: (x[1], x[0]))  # Sort by clock and process_id
            if self.current_process is None or self.request_queue[0][0] == process_id:
                self.current_process = process_id
                # Send REPLY message to the process
                bGrant = True
                print ("clsLab4MaekawaManager:grantEntry() " + " Granted entry to Critical section for the process id P" + str(process_id ))
            else:
                print ("clsLab4MaekawaManager:grantEntry() " + " Not Granted entry to Critical section for the process id P" + str(process_id ))
                bGrant = False

        except Exception as error:
            print("clsLab4MaekawaManager.grantEntry(): Process getEntry failed.")
            print (error)
        finally:
            print("clsLab4MaekawaManager.grantEntry(): Process getEntry completed successfully.")

        return bGrant
        