#S3C3 Dennis
#Task 27.06

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
 
