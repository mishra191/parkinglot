from agent.ParkingAgent import ParkingAgent


class Main:
    
    def __init__(self):
        self.parkingAgent = ParkingAgent()

    def run(self, ruleFile):
        self.parkingAgent.allocateParking()
        self.parkingAgent.loadRules(ruleFile)

    def allocateParking(self):
        self.parkingAgent.allocateParking()

    def reserveParking(self, time, vehicleType, sortingAlgo):
        return self.parkingAgent.reserveParking(vehicleType, sortingAlgo, time)

    def unReserveParking(self, parkingTicket, outTime):
        return self.parkingAgent.unReserveParking(parkingTicket, outTime)


   
               

                 

           
    
    
   
    
    