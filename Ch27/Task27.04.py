#S3C3 Dennis
#Task27.04

def PrintDetails(self):
    print('BookDetails')
    LibraryItem.PrintDetails(self)
    print(self.__IsRequested)

def PrintDetails(self):
    print("About CD")
    LibraryItem.PrintDetails(self)
    print(self.__Genre)
