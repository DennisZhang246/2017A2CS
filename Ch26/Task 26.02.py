#S3C3 Dennis
# Task 26.02

import pickle
import datetime


FileSize=100
class CarRecord :
    def __init__(self) :
        VehicleID = ""
        VehicleID = VehicleID.ljust(20)
        self.VehicleID = VehicleID.encode('utf-8')
        Registration = ""
        Registration = Registration.ljust(10)
        self.Registration = Registration.encode('utf-8')
        self.DateOfRegistration = datetime.datetime(2018,1,1)
        self.EngineSize = 0
        self.PurchasePrice = 0.0
        
    def Initialise() :
       CarFile = open('CarFile.DAT','wb')
       for i in range(100):
          Address = i * FileSize + 1
          CarFile.seek(Address, 0)
          pickle.dump(CarRecord(), CarFile)
       CarFile.close()
       
    def EstablishNewRecord() :
        ThisCar = CarRecord()
        VehicleID = input('Vehicle ID: ')
        VehicleID = VehicleID.ljust(20)
        ThisCar.VehicleID = VehicleID.encode('utf-8')
        Registration = input('Registration: ')
        Registration = Registration.ljust(10)
        ThisCar.Registration = Registration.encode('utf-8')
        ThisCar.DateOfregistration =(input('Registration Date: '));
        ThisCar.EngineSize = int(input('Engine size: '))
        ThisCar.PurchasePrice = float(input('Purchaseprice: '))
        return ThisCar

    def HashFunction(reg) :
       result = ord(reg[0]) * FileSize + 1
       print(result)
       return result

    def Save(ThisCar, CarFile) :
        Address = Hash(ThisCar.Registration.decode('utf-8'))
        CarFile.seek(Address, 0)
        pickle.dump(ThisCar, CarFile)
        
    def OpenFile() :
        CarFile = open('CarFile.DAT','rb+')
        return CarFile

    def FindRecord(reg, CarFile) :
       Address = Hash(reg)
       CarFile.seek(Address, 0)
       ThisCar = pickle.load(CarFile)
       return ThisCar
    
    def OutputData(ThisCar) :
       print(ThisCar.VehicleID)

    def main() :
        Initialise()
        CarFile = OpenFile()
        ThisCar = CarRecord()
        show = input("add a record? Type in 'Y' for Yes and 'N' for No.")
        while not show == 'N' :
            ThisCar = CarRecord()
            ThisCar = EstablishNewRecord()
            SaveToFile(ThisCar, CarFile)
            show = input("add a record? Type in 'Y' for Yes and 'N' for No.")
            show = input("find a record? Type in 'Y' for Yes and 'N' for No.")
        while not show == 'N' :
            Reg = input('Give vehicle registration: ')
            ThisCar = FindRecord(Reg, CarFile)
            OutputData(ThisCar)
            show = input("find a record? Type in 'Y' for Yes and 'N' for No.")
        CarFile.close()
   
