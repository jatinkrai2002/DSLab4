
# lab 4
# . Process Interface: This interface defines methods for processes to interact with the mutual exclusion logic.
# Name: Jatin K rai
#DawID

"""
Process Interface: This interface defines methods for processes to interact with the mutual exclusion logic. Methods can include:
• requestCriticalSection(): Requests entry to the critical section.
• releaseCriticalSection(): Releases control after exiting the critical section.
• getQuorum(): Retrieves the process IDs belonging to the quorum this process uses (optional, can be pre-configured).


"""
import Pyro5.api

class iLab4MaekawaMutualExclusion:
    @Pyro5.api.expose
    def requestCriticalSection(self):
        pass

    @Pyro5.api.expose
    def releaseCriticalSection(self):
        pass

    @Pyro5.api.expose
    def getQuorum(self):
        pass