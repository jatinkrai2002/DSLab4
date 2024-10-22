
# lab 3
# ProcessMaekawaMutualExclusionClient: This is act as Client Process.  
# Name: Jatin K rai
#DawID

"""
# Process Implementation client:  This class implements the Process interface. It maintains: . 
"""

import Pyro5.api
from clsLab4MaekawaMutualExclusionP2 import clsLab4MaekawaMutualExclusionP2

def start_ProcessMaekawaMutualExclusionClient():
    try:
        uri = input("Enter the UnicastRemoteObject for Maekawa Mutual Exclusion URI: ")
       # numberofprocess = int(input("Please enter the number of process such as 3: including quorum:"))
        numberofprocess = 3 #Consider only for 3 process.

        remote_processP2 = clsLab4MaekawaMutualExclusionP2(uri, numberofprocess)

        processidrequestforCS = 2 # process id
        print ("clsLab4MaekawaMutualExclusion:requestCriticalSection has started  for Process P2")
        print ("Quorom for process 3 as preconfigured ")
        print ( "for P0 the quorum will be (1,2)")
        print ("for P1 the quorum will be (0.2)")
        print ("for P2 the quorum will be (0,1)")
        remote_processP2.requestCriticalSection(processidrequestforCS)
        print ("clsLab4MaekawaMutualExclusion:requestCriticalSection has completed  for Process P2")

        processidreleasefromCS = 2 # process id
        # Simulate critical section work
        print ("clsLab4MaekawaMutualExclusion:releaseCriticalSection has started  for Process P2")
        remote_processP2.releaseCriticalSection(processidreleasefromCS)
        print ("clsLab4MaekawaMutualExclusion:releaseCriticalSection has completed  for Process P2")
    except Exception as error:
            print("Pyro5.api.Proxy(): start_ProcessMaekawaMutualExclusionClient Pyro5.api.Proxy failed while calling")
            print (error)
    finally:
            print("Pyro5.api.Proxy(): start_ProcessMaekawaMutualExclusionClient Pyro5.api.Proxy completed successfully while calling.")
   

if __name__ == "__main__":
    start_ProcessMaekawaMutualExclusionClient()
