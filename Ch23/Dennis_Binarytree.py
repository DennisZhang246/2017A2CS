#S3C3 Dennis
# Dry Run
nullptr=-1
class Listnode(object):
    def _init_(self,data,rightptr,leftptr):
        self.data = data
        self.leftpointer=leftpointer
        self.rightpointer=rightpointer

list=[0]*7
for i in range(7):
    list[i]=Listnode('','','')

    def Initialise():
        global freeptr,rootptr
        rootptr=nullptr
        freeptr=-1
        for i in range (6):
            Tree[i].LeftPointer=i+1
        Tree[7].leftptr=nullptr

    def insertnode(newitem):
        global freeptr,rootptr
        if not freeptr==nullptr:
            newnodeptr=freeptr
            freeptr=Tree[freeptr].leftptr
            Tree[newnodeptr].data=newitem
            Tree[newnodeptr].leftptr=nullptr
            Tree[newnodeptr].rightptr=nullptr
            if rootptr==nullptr:
                rootptr=newnodeptr
                thisnodeptr=rootptr
                while not thisnodeptr==nullptr:
                    previous=thisnodeptr
                    if Tree[thisnodeptr].Data>newitem:
                        goleft=True
                        thisnodeptr=Tree[thisnodeptr].leftptr
                    else:
                        goleft=False
                        thisnodeptr=Tree[thisnodeptr].rightptr
                if goleft==True:
                    Tree[previous].leftptr=newnodeptr
                else:
                    Tree[previous].rightptr=newnodeptr

    def find(searchitem):
        global freeptr,rootptr
        thisnodeptr=rootptr
        while not thisnodeptr==nullptr and not Tree[thisnodeptr].Data==searchitem:
            if Tree[thisnodeptr].Data>searchitem:
                thisnodeptr=Tree[thisnodeptr].leftptr
            else:
                thisnodeptr=Tree[thisnodeptr].rightptr

initialise()
insertnode()
find()
            
        
    
        

    
        
