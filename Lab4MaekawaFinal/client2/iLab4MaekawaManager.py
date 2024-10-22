
# lab 4
# MaekawaManager Interface: This interface (optional) can be used for centralized management   
# Name: Jatin K rai
#DawID

"""
MaekawaManager Interface: This interface (optional) can be used for centralized management 
(useful for smaller systems). Methods can include:
• grantEntry(processId, clock): Processes a grant request from a process after receiving enough votes.


"""

import Pyro5.api

class iLab4MaekawaManager:
    @Pyro5.api.expose
    def grantEntry(self, process_id, clock):
        pass