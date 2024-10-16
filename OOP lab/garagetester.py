from truck import Truck
from garage import Garage

class GarageTester:
    def getExample(self):
        truck1=Truck('black')
        garage1=Garage()
        garage1.setVehicle(truck1)
        return garage1
    