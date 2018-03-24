#Task 2

### 2.1
Toy:
GetName()
GetID()
GetPrice()
GetMinWage()
-------------
SetName()
SetID()
SetPrice()
SetMinWage()

ComputerGame:
GetCategory()
GetConsole()
-------------
SetCategory()
SetConsole()

Vehicle:
GetType()
GetHeight()
GetLength()
GetWeight()
-----------
SetType()
SetHeight()
SetLength()
SetWeight()



### 2.2
The code for the base class is only written once and the subclasses make use of the attributes and methods of the base class, as well as having their own attributes and methods. 

### 2.3
class Toy:
    def __init__(self,n,i,p,w):
        self.__name=n
        self.__id=i
        self.__price=p
        self.__minimumage=w
    
    def GetName(self):
        return self.__name
        
    def SetName(self,name):
        self.__name=name
        
    def GetID(self):
        return self.__id
    
    def SetID(self,id):
        self.__id=id
    
    def GetPrice(self):
        return self.__price
        
    def SetPrice(self,price):
        self.__price=price
    
    def GetMinWagee(self):
        return self.__wage
   
    def SetMinWage(self,min):
        self.__wage=wage

### 2.4
class ComputerGame(Toy):
    def _init_(self,n,i,p,w):
	Toy._init_(self,n,i,p,w)
	self.__category= ''
	self.__console=''

    def GetCategory(self):
	return self.__category

    def SetCategory(self,category)
	self.__category=category

    def GetConsole(self):
	return self.__console

    def SetConsloe(self,console)
	self.__console=console

class Vehicle(Toy):
    def _init_(self,n,i,p,w):
	Toy._init_(self,n,i,p,w)
	self.__type= ''
	self.__height=0
	self.__length=0
	self.__weight=0

    def GetType(self):
	return self.__type

    def SetType(self,type)
	self.__type=type
	
    def GetHeight(self):
	return self.__height

    def SetHeight(self,height)
	self.__height=height

    def GetLength(self):
	return self.__Length

    def SetLength(self,length)
	self.__length=length

    def GetWeight(self):
	return self.__weight

    def SetWeight(self,weight)
	self.__weight=weight

###2.5

###2.6
def main()
    toy1=vechile('Red Sport Car',10)
    toy1.type('Car')
    toy1.height(3.3)
    toy1.length(12.1)
    toy1.weight(0.08)

###2.7
def printdetails(id):
   i=0
   while toy[i].id!=id and i<len(toy)
        i+=1
   toy[i].printdetails()

###2.8
def discount(n):
    n=n/100
    for i in range(len(toy)):
        toy[i].SetPrice(toy[i].GetPrice()*n)

###2.9
Bubble sort: Exchange the position of the largest value to the end of the array at first loop. The other values may or may not be in the correct order.
By working through the array again and again, the array the next largest value will be in its correct position and all values will be in order.

Insertion sort: Moving the current card down a position. If the value of the card to be inserted is smaller than the last card you considered, then the card is inserted at the top of the pile.

###2.10
def sort():
    for i in range(1,len(toys)):
        itemtobeinserted=toy[i]
        c=i-1
    




