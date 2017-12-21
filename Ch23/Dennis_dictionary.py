#S3C3 Dennis

class dictionary():
    def _init_(self):
        self.abb=''
        self.term=''


dictionary=[dictionary() for i in range(20)]
for index in range(20):
    dictionary[index].abb=None
    dictionary[index].term=None
    

def insert(a,t):#abb=abbreviation
    
    index=(ord(a[1])-ord(a[0]))%20
    dictionary[index].abb=a
    dictionary[index].term=t
    while dictionary[index].abb != None:
        index=index+1
        if index>20:
            index=0
    dictionary[index]=dictionary

def translate(abb):
   index=(ord(abb[1])-ord(abb[0]))%20
   while not dictionary[index] ==abb and dictionary[index]!=0:
        index=index+1
        if index>20:
            index=0
   if dictionary[index]!=None:
        return dictionary[index].value
   else:
        return 'the abbreviation is not found'


   
insert('alu','Alrithmatic logical unit')
