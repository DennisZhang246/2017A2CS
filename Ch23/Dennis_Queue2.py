#S3C3 Dennis
# Queue
class Node():
    def __init__(self):
        self.Next=None
        self.content=None

def _init_():
    global Nullpointer,StartPointer,FreeListPointer,full,List,RealPtr
    Nullpointer=-1
    StartPointer=Nullpointer
    RealPtr=0
    FreeListPointer=0
    List=[0]*10
    full=0
    for i in range(10):
        List[i]=Node()
        List[i].Next=i+1
    List[9].Next=Nullpointer

def Push(NewItem):
    global Nullpointer,StartPointer,FreeListPointer,full,List,RealPtr
    EndlistPtr=full
    if full==10:
        print("No extra space")
    elif StartPointer==Nullpointer:
        StartPointer=0
        List[0].Next=Nullpointer
        List[FreeListPointer].content=NewItem
        FreeListPointer=1
        full=full+1
    else:
        ThisNodePtr=RealPtr
        full=full+1
        RealPtr=FreeListPointer
        List[ThisNodePtr].Next=FreeListPointer
        List[FreeListPointer].content=NewItem
        Previous=FreeListPointer
        FreeListPointer=List[FreeListPointer].Next
        List[Previous].Next=Nullpointer

def Pop():
    global Nullpointer,StartPointer,FreeListPointer,full,List,RealPtr
    full=full-1
    if not full==0:
        ThisNodePtr=StartPointer
        List[ThisNodePtr].content=None
        StartPointer=List[ThisNodePtr].Next
        

def Print():
    global Nullpointer,StartPointer,FreeListPointer,full,List,RealPtr
    NewItem=StartPointer
    for i in range(full):
        print(List[NewItem].content,end="   " )
        NewItem=List[NewItem].Next
    print("")



_init_()
Push(2)
Push(4)
Push(6)
Push(1)
Push(6)
Push(5)
Pop()
Pop()
Pop()
Push(6)
Push(4)
Print()
Push(2)
Print()
Push(5)
Print()
Pop()
Pop()
Push(6)
Push(4)
Print()
Push(2)
Print()
Push(5)
Print()
