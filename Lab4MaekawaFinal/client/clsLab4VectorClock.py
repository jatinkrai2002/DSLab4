# lab 4
# . VectorClock Interface: This interface defines methods for managing vector clocks (as described previously).  
# Name: Jatin K rai
#DawID

"""
# Process Implementation: This class implements the Process interface. It maintains: 
• A local VectorClock object (see below). 
VectorClock Interface: This interface defines methods for managing vector clocks 
increment()
get_time()


"""


import Pyro5.api
from iLab4VectorClock import iLab4VectorClock

# implement class witn instance_mode single.
# pyro objects for instance_mode=single (singletons, just one per daemon)
# @Pyro5.api.behavior(instance_mode="single")

class clsLab4VectorClock(iLab4VectorClock):
    P0clock = 0
    P1clock = 0
    P2Clock = 0
    
    def __init__(self):
        #define clock for each process P0,P1, P2
        self.P0clock = 0
        self.P1clock = 0
        self.P2clock = 0

    #increment local time based on process id.
    def increment(self, process_id):
        try:
            if (process_id == 0):
                self.P0clock += 1
            elif (process_id == 1):
                self.P1clock += 1
            elif (process_id == 2):
                self.P2clock += 1
            else:
               self.P0clock += 1 # default Process 0
            
            print("VectorClock increment for - process id  : ", process_id)

        except Exception as error:
            print("VectorClock.increment(): Process  failed.")
            print (error)
        finally:
            print("VectorClock.increment(): Process completed successfully.")

  #get time of local value
    def get_time(self, process_id):
        retunrnval = 0
        try:
            if (process_id == 0):
                retunrnval = self.P0clock
            elif (process_id == 1):
                retunrnval = self.P1clock
            elif (process_id == 2):
                retunrnval = self.P2clock
            else:
                retunrnval = self.P0clock1 # default Process 0
            
            print("VectorClock gettime for - process id  : ", process_id)
        except Exception as error:
            print("VectorClock.getitme(): Process  failed.")
            print (error)
        finally:
            print("VectorClock.gettime(): Process completed successfully.")
    
        return retunrnval
    