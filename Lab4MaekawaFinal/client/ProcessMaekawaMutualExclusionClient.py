
# lab 3
# ProcessMaekawaMutualExclusionClient: This is act as Client Process.  
# Name: Jatin K rai
#DawID

"""
# Process Implementation client:  This class implements the Process interface. It maintains: . 
"""

import Pyro5.api
from clsLab4MaekawaMutualExclusion import clsLab4MaekawaMutualExclusion


def start_ProcessMaekawaMutualExclusionClient():
    try:
        uri = input("Enter the UnicastRemoteObject for Maekawa Mutual Exclusion URI: ")
      #  numberofprocess = int(input("Please enter the number of process such as 3: including quorum "))
        numberofprocess = 3 #Consider only for 3 process.
       # remote_process = Pyro5.api.Proxy(uri)
        remote_process = clsLab4MaekawaMutualExclusion(uri, numberofprocess)

        processidrequestforCS = int(input("Please enter the process number(0 to 2) (total processes is 3) to request for Critical Section: "))
        # Assume same process will release from Queue.
        print ("clsLab4MaekawaMutualExclusion:requestCriticalSection has started ")
        print ("Quorom for process 3 as preconfigured ")
        print ( "for P0 the quorum will be (1,2)")
        print ("for P1 the quorum will be (0.2)")
        print ("for P2 the quorum will be (0,1)")
        remote_process.requestCriticalSection(processidrequestforCS)
        print ("clsLab4MaekawaMutualExclusion:requestCriticalSection has completed ")

        #processidrequestforCS = int(input("Please enter the process number(0 to 2) (total processes is 3) to release from Critical Section: "))
        # Assume same process will release from Queue.
        # Simulate critical section work
        print ("clsLab4MaekawaMutualExclusion:releaseCriticalSection has started ")
        remote_process.releaseCriticalSection(processidrequestforCS)
        print ("clsLab4MaekawaMutualExclusion:releaseCriticalSection has completed ")

        """
        # Commented code and used as seperate client for P0, P1 and P2.
            remote_processP0 = clsLab4MaekawaMutualExclusionP0(uri, numberofprocess)

            processidrequestforCS = int(input("Please enter the process number(0 to 2) (total processes is 3) to request for Critical Section: "))
            print ("clsLab4MaekawaMutualExclusion:requestCriticalSection has started ")
            print ("Quorom for process 3 as preconfigured ")
            print ( "for P0 the quorum will be (1,2)")
            print ("for P1 the quorum will be (0.2)")
            print ("for P2 the quorum will be (0,1)")
            remote_processP0.requestCriticalSection(processidrequestforCS)
            print ("clsLab4MaekawaMutualExclusion:requestCriticalSection has completed ")

            processidreleasefromCS = int(input("Please enter the process number(0 to 2) (total processes is 3) to release from Critical Section: "))
            # Simulate critical section work
            print ("clsLab4MaekawaMutualExclusion:releaseCriticalSection has started ")
            remote_processP0.releaseCriticalSection(processidreleasefromCS)
            print ("clsLab4MaekawaMutualExclusion:releaseCriticalSection has completed ")


            remote_processP1 = clsLab4MaekawaMutualExclusionP1(uri, numberofprocess)

            processidrequestforCS = int(input("Please enter the process number(0 to 2) (total processes is 3) to request for Critical Section: "))
            print ("clsLab4MaekawaMutualExclusion:requestCriticalSection has started ")
            print ("Quorom for process 3 as preconfigured ")
            print ( "for P0 the quorum will be (1,2)")
            print ("for P1 the quorum will be (0.2)")
            print ("for P2 the quorum will be (0,1)")
            remote_processP1.requestCriticalSection(processidrequestforCS)
            print ("clsLab4MaekawaMutualExclusion:requestCriticalSection has completed ")

            processidreleasefromCS = int(input("Please enter the process number(0 to 2) (total processes is 3) to release from Critical Section: "))
            # Simulate critical section work
            print ("clsLab4MaekawaMutualExclusion:releaseCriticalSection has started ")
            remote_processP1.releaseCriticalSection(processidreleasefromCS)
            print ("clsLab4MaekawaMutualExclusion:releaseCriticalSection has completed ")

            remote_processP2 = clsLab4MaekawaMutualExclusionP2(uri, numberofprocess)

            processidrequestforCS = int(input("Please enter the process number(0 to 2) (total processes is 3) to request for Critical Section: "))
            print ("clsLab4MaekawaMutualExclusion:requestCriticalSection has started ")
            print ("Quorom for process 3 as preconfigured ")
            print ( "for P0 the quorum will be (1,2)")
            print ("for P1 the quorum will be (0.2)")
            print ("for P2 the quorum will be (0,1)")
            remote_processP2.requestCriticalSection(processidrequestforCS)
            print ("clsLab4MaekawaMutualExclusion:requestCriticalSection has completed ")

            processidreleasefromCS = int(input("Please enter the process number(0 to 2) (total processes is 3) to release from Critical Section: "))
            # Simulate critical section work
            print ("clsLab4MaekawaMutualExclusion:releaseCriticalSection has started ")
            remote_processP2.releaseCriticalSection(processidreleasefromCS)
            print ("clsLab4MaekawaMutualExclusion:releaseCriticalSection has completed ")
        """
    except Exception as error:
            print("Pyro5.api.Proxy(): start_ProcessMaekawaMutualExclusionClient Pyro5.api.Proxy failed while calling")
            print (error)
    finally:
            print("Pyro5.api.Proxy(): start_ProcessMaekawaMutualExclusionClient Pyro5.api.Proxy completed successfully while calling.")
    # uri = "PYRONAME:Maekawa.clsLab4MutecxManager"
   

if __name__ == "__main__":
    start_ProcessMaekawaMutualExclusionClient()
