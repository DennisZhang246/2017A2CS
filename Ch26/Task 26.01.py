#S3C3 Dennis Zhang
#Task 26.01

import pickle 
import datetime

class CarRecord:
    
   def __init__(self):
       self.VehicleID = ""
       self.Registration = ""
       self.DateOfRegistration = datetime.datetime(2018,1,1)
       self.EngineSize = 0
       self.PurchasePrice = 0
       
   def Save(Car):
       CarFile = open('CarFile.DAT','wb')
       for i in range(100): 
          pickle.dump(Car[i], CarFile)
       CarFile.close()
   
   def Load():
          CarFile = open('CarFile.DAT','rb') 
          Car = []
          Check = False
          while Check == False:
              if not Car.append(pickle.load(CarFile)):
                  Check = True
          CarFile.close()
          return Car
        
   def Print(Car) :
       for i in range(100):
           print(Car[i].VehicleID)
           
   def main():
       ThisCar = CarRecord()
       Car = [ThisCar for i in range(100)]
       SaveData(Car)
       Car = LoadData()
       OutputRecords(Car)
       go = int(input('Type in an record number.'))
       while i != 0 :
            Car[i].VehicleID = input('Vehicle ID: ')
            Car[i].Registration = input('Registration: ')
            Car[i].DateOfregistration = (input('Date of Registration: '));
            Car[i].EngineSize = int(input('Engine size: '))
            Car[i].PurchasePrice = float(input('Price: '))
            go = int(input('Type in an record number.'))
       print('You quit the system.')
       OutputRecords(Car)
       SaveData(Car)
        
