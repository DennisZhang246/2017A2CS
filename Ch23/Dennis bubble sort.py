def bubble(bblist):
    length = len(bblist)
    for i in range(length):
        k=0
        k+=0
        for j in range(length - k-1):
            if bblist[j] > bblist[j+1]:
                a=bblist[j]
                bblist[j]=bblist[j+1]
                bblist[j+1]=a
    return bblist
 

