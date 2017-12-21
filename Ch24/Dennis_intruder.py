#S3C3 Dennis

class Node():
    def __init__(self):
        self.Next=None
        self.content=None

def init():
    global Nullpointer,StartPointer,FreeListPointer,full,List
    Nullpointer=-1
    StartPointer=Nullpointer
    FreeListPointer=0
    List=[0]*10
    full=0
    for i in range(10):
        List[i]=Node()
        List[i].Next=i+1
    List[9].Next=Nullpointer

def Push(NewItem):
    global Nullpointer,StartPointer,FreeListPointer,full,List
    if full==10:
        print("List is fulfilled")
    elif StartPointer==Nullpointer:
         full=full+1
         StartPointer=0
         List[0].Next=Nullpointer
         List[FreeListPointer].content=NewItem
         FreeListPointer=1

    else:
        full=full+1
        while List[StartPointer].content>NewItem:
            List[FreeListPointer].Next=StartPointer
            StartPointer=FreeListPointer
        else:
            ThisNodePtr=StartPointer
            check=True
            for i in range(full-1):
                if List[ThisNodePtr].content<NewItem:
                    Previous=ThisNodePtr
                    ThisNodePtr=List[ThisNodePtr].Next
                if List[ThisNodePtr].content>NewItem:
                    check=False
            if check==True:
                List[ThisNodePtr].Next=FreeListPointer
                List[FreeListPointer].content=NewItem
                Previous=FreeListPointer
                FreeListPointer=List[FreeListPointer].Next
                List[Previous].Next=Nullpointer
            if check==False:
                List[Previous].Next=FreeListPointer
                List[FreeListPointer].content=NewItem
                Previous=FreeListPointer
                FreeListPointer=List[FreeListPointer].Next
                List[Previous].Next=ThisNodePtr

def Pop(NewItem):
    global Nullpointer,StartPointer,FreeListPointer,full,List
    if not SearchNode(NewItem)==None:
        full=full-1
        if NewItem==List[StartPointer]:
            StartPointer=List[StartPointer].Next
        else:
            ThisNodePtr=StartPointer
            while NewItem!=List[ThisNodePtr].content:
                Previous=ThisNodePtr
                ThisNodePtr=List[ThisNodePtr].Next
            List[Previous].Next=List[ThisNodePtr].Next
            i=FreeListPointer
            while List[i].Next!=Nullpointer:
                i=List[i].Next
            List[i].Next=ThisNodePtr
            List[ThisNodePtr].Next=Nullpointer

def Print():
    global Nullpointer,StartPointer,FreeListPointer,full,List
    NewItem=StartPointer;
    for i in range(full):
        print(List[NewItem].content,end="   ")
        NewItem=List[NewItem].Next


init()
Push(1)
Push(2)
Push(3)
Push(4)
Push(5)
Push(6)
Print()
Pop(2)
Print()



