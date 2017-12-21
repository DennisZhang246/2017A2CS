#S3C3 Dennis
class Node():
    def __init__(self):
        self.Next=None
        self.content=None

def _init_():
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
        print("List is fulfilled.")
    elif StartPointer==Nullpointer:
        StartPointer=0
        List[0].Next=Nullpointer
        List[FreeListPointer].content=NewItem
        FreeListPointer=1
        full=full+1
    else:
        ThisNodePtr=StartPointer
        full=full+1
        while not List[ThisNodePtr].Next==Nullpointer:
            ThisNodePtr=List[ThisNodePtr].Next
        List[ThisNodePtr].Next=FreeListPointer
        List[FreeListPointer].content=NewItem
        Previous=FreeListPointer
        FreeListPointer=List[FreeListPointer].Next
        List[Previous].Next=Nullpointer

def Pop():
    global Nullpointer,StartPointer,FreeListPointer,full,List
    full=full-1
    if not full==0:
        ThisNodePtr=StartPointer
        while not List[ThisNodePtr].Next==Nullpointer:
            Previous=ThisNodePtr
            ThisNodePtr=List[ThisNodePtr].Next
        List[Previous].Next=Nullpointer
        List[ThisNodePtr].Next=FreeListPointer
        FreeListPointer=ThisNodePtr
        List[ThisNodePtr].content=None
        print(FreeListPointer)

def Print():
    global Nullpointer,StartPointer,FreeListPointer,full,List
    NewItem=StartPointer
    for i in range(full):
        print(List[NewItem].content,end="   ")
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


