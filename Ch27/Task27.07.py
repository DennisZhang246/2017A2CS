#S3C3 Dennis
#TAsk 27.07
#Not Finished

import datetime
class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author_Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()
        
    def GetTitle(self):
        return(self.__Title)

    def GetAuthor_Artist(self):
        return(self.__Author_Artist)

    def GetItemID(self):
        return(self.__ItemID)

    def GetOnLoan(self):
        return(self.__OnLoan)

    def GetDueDate(self):
        return(self.__DueDate)
    
    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)
        
    def Returning(self):
        self.__OnLoan = False
        
    def PrintDetails(self):
        print(self.__Title, ' ; ', self.__Author_Artist,end='')
        print(' ; ', self.__ItemID, ' ; ', self.__OnLoan,end='')
        print(' ; ', self.__DueDate)
        
class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False

    def GetIsRequested(self):
        return(self.__IsRequested)

    def SetIsRequested(self):
        self.__IsRequested = True
        
class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""
        
    def GetGenre(self):
        return(self.__Genre)
    def SetGenre(self, g):
        self.__Genre = g

class Borrower() :
    def __init__(self, a, b, c) :
      self.__BorrowerName = a
      self.__EmailAddress = b
      self.__BorrowerID = c
      self.__ItemsOnLoan = 0
      
    def BorrowerName(self):
      return(self.__BorrowerName)
    
    def EmailAddress(self):
      return (self.__EmailAddress)
    
    def BorrowerID(self):
      return (self.__BorrowerID)
    
    def ItemsOnLoan(self):
      return(self.__ItemsOnLoan)
    
    def AddNewBorrower(self, n) :
      self.__ItemsOnLoan += n

    def Print(self):
       print('BorrowerName:',self.__BorrowerName)
       print('EmailAddress:',self.__EmailAddress)
       print('BorrrowerID:',self.__BorrowerID)
       print('ItemOnLoan:',self.__ItemsOnLoan)

class LibraryItem:
    def __init__(self, t, a, i): 
      self.__Title = t
      self.__Author_Artist = a
      self.__ItemID = i
      self.__OnLoan = False
      self.__DueDate = datetime.date.today()
      self.__BorrowerID = 0
      
    def BorrowerName(self):
      return(self.__BorrowerName)
    
    def EmailAddress(self):
      return (self.__EmailAddress)
    
    def BorrowerID(self):
      return (self.__BorrowerID)
    
    def ItemsOnLoan(self):
      return(self.__ItemsOnLoan)
    
    def AddNewBorrower(self, n) :
      self.__ItemsOnLoan += n
      
    def Borrowing(self, b):
      self.__OnLoan = True
      self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)
      self.__BorrowerID = b
      
    def Print(self):
       print('BorrowerName:',self.__BorrowerName)
       print('EmailAddress:',self.__EmailAddress)
       print('BorrrowerID:',self.__BorrowerID)
       print('ItemOnLoan:',self.__ItemsOnLoan)
       if self.OnLoan = True:
           print('DueDate:',self.__DueDate)

class Book(LibraryItem):   
   def __init__(self, t, a, i): 
      LibraryItem.__init__(self, t, a, i)
      self.__IsRequested = False
      self.__RequestedBy = 0
      
   def Get(self):
      return(self.__IsRequested)
    
   def Set(self, b):
      self.__IsRequested = True
      self.__RequestedBy = b
      
   def PrintDetails(self):
      print("Book Details")
      LibraryItem.PrintDetails(self)
      if self.__IsRequested = True:
         print('Requested by ', self.__RequestedBy)
      else :
         print('Not Found')

def main():
    
