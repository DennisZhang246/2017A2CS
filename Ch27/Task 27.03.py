#S3C3 Dennis
#Task 27.03

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

def test():
    test1 = Borrower('Gorfrey','@RDFZ','100000000')
    test1.AddNewBorrower(4)
    test1.Print()

test()
