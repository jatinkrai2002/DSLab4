
# lab 4
# ProcessMaekawaMutualExclusionServer  : This is act as Server process 
# Name: Jatin K rai
#DawID

"""
This is act as server process ProcessMaekawaMutualExclusionServer
"""

import Pyro5.api
from clsLab4MaekawaManager import clsLab4MaekawaManager

def main():
    #Act as Server.
    try:
        #make it server ready for remote process.
        daemon = Pyro5.api.Daemon()
    except Exception as error:
        print("rPyro5.api.Daemo(): failed.")
        print(error)
    finally:
        print("Pyro5.api.Daemo(): completed successfully.")

    try:
        #make it server ready for remote process.
        # Register Maekawa MutexManager
        Maekawamutex_manager = clsLab4MaekawaManager()
        uri = daemon.register(Maekawamutex_manager)
     #   daemon.register("clsLab4MaekawaMutualExclusion.clsLab4MaekawaManager", uri)

    except Exception as error:
        print("Pyro5.api.Daemo.register(): failed.")
        print(error)
    finally:
        print("Pyro5.api.Daemo.register() : completed successfully.")
        
    try:
        #make it server ready for remote process.
        print("UnicastRemoteObject for Maekawa MutualExclusion  Protocol=" , uri)
        print(" Maekawa Manager  Exclusion registered. Ready.")
        daemon.requestLoop()  # Start the event loop of 
    except Exception as error:
        print("Pyro5.api.Daemo.requestLoop(): failed.")
        print(error)
    finally:
        print("Pyro5.api.Daemo.requestLoop() : clsLab4 Maekawa Manager completed successfully.")

if __name__ == "__main__":
    main()