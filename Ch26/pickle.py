#S3C3 Dennis Zhang
#pickle

class CarRecord:
    def _init_(self):
        self.VehicleID = ""
        self.Registration= ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self .PurchasePrice = 0.00

ThisCar = CarRecord()
ThisCar.engineSize = 2500

ThisCar = CarRecord()
Car = [ThisCar for i in range(100)]
Car[1].EngineSize = 2500

import pickle
ThisCar = CarRecord()
Car = [ThisCar for i in range(100)]

CarFile = open('Cars.DAT','wb')
for i in range(100):
    pickle.dump(Car[i],CarFile)
CarFile.close()

CarFile = open('Cars.DAT','rb')

Car = []
for i in range(100):
    Car.append(pickle.load(CarFile))

CarFile.close()
