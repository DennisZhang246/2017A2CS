#S3C3 Dennis
# Library

import datetime
class LibraryItem:
    def _init_(self,t,a,i):
        self. Title = t
        self. AuthorArtist = a
        self. ItemID = i

    def GetTitle(self):
        return(self._Title)

    def Borrowing(self):
        self. OnLoan = True
        self. DueDate = self. DueDate + datetime.timedelta(weeks=3)
        
    def Returning(self):
        self. OnLoan = False

    def PrintDetails(self):
        print(self._Title,'; ',self._Author_Artist,'; ',end='')
        print(self._ItemID,'; ',self._OnLoan,'; ',self._DueDate)

class Book(LibraryItem):
    def _init_(self,t,a,i):
        LibraryItem. init (self, t, a, i)
        self._IsRequested = False
        self._RequestedBy = O

    def GetisRequested(self):
        return (self. IsRequested)

    def SetisRequested(self):
        self. IsRequested = True

class CD(LibraryItem):
    def _init_(self, t, a, i):
        LibraryItem._init_(self, t, a, i)
        self. Genre= ""
    def GetGenre (self):
        return (self._Genre)
    def SetGenre (self, g):
        self. Genre= g

