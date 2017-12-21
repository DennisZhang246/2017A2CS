#S3C3 Dennis
#Codingbat Recursion1

def factorial(n):
    if n==1:
        return 1
    return n*(factorial(n-1))

print(factorial(6))

def bunnyEars(n):
    if n==0:
        return 0
    return 2+bunnyEars(n-1)

print(bunnyEars(6))

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(6))

def bunnyEars2(n):
    if n==0:
        return 0
    elif n%2==1:
        return 2+bunnyEars2(n-1)
    return 3+bunnyEars2(n-1)

print(bunnyEars2(6))

def triangle(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return n+triangle(n-1)

print(triangle(6))

def sumDigits(n):
    if n==0:
        return 0
    return n%10+sumDigits(n//10)

print(sumDigits(1206))

def count7(n):
    if n==0:
        return 0
    if n%10==7:
        return 1+count7(int(n/10))
    else:
        return count7(int(n/10))

print(count7(761727))

def count8(n):
    if n==8:
        return 1
    if n%100==88:
        return 2+count8(n//10)
    if n%10==8:
        return 1+count8(n//10)

    return count8(n//10)

print(count8(8188298))

def powerN(base,n):
    if n==1:
        return base
    n = n - 1
    return base*powerN(base,n)
def powerN(base,n):
    if n==1:
        return base
    return base*powerN(base,n-1)

print(powerN(3,3))

def countX(n):
    if n=="":
        return  0
    elif n[len(n)-1]=='x':
        return 1+countX(n[0:len(n)-1])
    else:
        return countX(n[0:len(n)-1])
        
print(countX('axcxscxvx'))

def countHi(n):
    if n=="":
        return  0
    elif len(n)>=2 and n[-2]=='H' and n[-1]=='i':
        return countHi(n[:-1])+1
    else:
        return countHi(n[:-1])
        
print(countHi('xHimmHilHio'))

def changeXY(n):
    if n=="":
        return  ''
    elif n[len(n)-1]=='x':
        return changeXY(n[:-1])+'y'
    else:
        return changeXY(n[:-1])+n[-1]

print(changeXY('abxxyc'))
    
def changePi(n):
    if n=="":
        return  ''
    elif len(n)>=2 and n[len(n)-2]=='p' and n[len(n)-1]=='i':
        return changePi(n[:-2])+'3.14'
    else:
        return changePi(n[:-1])+n[-1]
    
print(changePi('apibpic'))

def noX(n):
    if n=='':
        return ''
    if n[-1]=='x':
        return noX(n[:-1])
    else:
        return noX(n[:-1])+n[-1]

print(noX('zaxcxsx'))

def array6(n,index):
    if index>=len(n)-1 and n[index]!=6:
        return False
    elif n[index]==6:
        return True
    else:
        return array6(n,index+1)
    
print(array6([1,2,4,5,7,6],0))

def array11(n,index):
    if index>=len(n)-1 and n[index]==11:
        return 1
    if index>=len(n)-1 and n[index]!=11:
        return 0
    elif n[index]==11:
        return 1+array11(n,index+1)
    else:
        return array11(n,index+1)
    
print(array11([11,2,11,3,4,5,11],0))

def array220(n,index):
    if index>=len(n)-1 and n[index]%10!=0:
        return False
    elif n[index]%10==0:
        return True
    else:
        return array220(n,index+1)
    
print(array220([1,2,4,5,7,60],0))

def allStar(n):
    if len(n)-1<=0:
        return n[0]
    return allStar(n[:-1])+"*"+n[-1]

print(allStar('chenkewei'))

def pairStar(n):
    if len(n)-1<=0:
        return n[0]
    if n[-1]==n[-2]:
        return pairStar(n[:-1])+"*"+n[-1]
    else:
        return pairStar(n[:-1])+n[-1]

print(pairStar('cckkwei'))

def endX(n):
    if n=='':
        return ''
    if n[0]=='x':
        return endX(n[1:])+'x'
    else:
        return n[0]+endX(n[1:])

print(endX('xcbvxdsxbn'))

def countPairs(n):
    if len(n)<=2:
        return 0
    if n[-1]==n[-3]:
        return 1+countPairs(n[:-1])
    else:
        return countPairs(n[:-1])

print(countPairs('bxaxa'))

def countAbc(n):
    if len(n)<=2:
        return 0
    if n[-1]=='c' and n[-2]=='b' and n[-3]=='a':
        return 1+countAbc(n[:-1])
    elif n[-1]=='a' and n[-2]=='b' and n[-3]=='a':
        return 1+countAbc(n[:-1])
    else:
        return countAbc(n[:-1])

print(countAbc('ababc'))

def count11(n):
    if len(n)<=1:
        return  0
    elif len(n)>=2 and n[-2]=='1' and n[-1]=='1':
        return count11(n[:-2])+1
    else:
        return count11(n[:-1])

print(count11('a11bc1111d'))

def stringclean(n):
    if len(n)<=2:
        return n[0]
    if n[-1]==n[-2] and n[-1]==n[-3]:
        return stringclean(n[:-3])+n[-1]
    elif n[-1]==n[-2]:
        return stringclean(n[:-2])+n[-1]
    else:
        return stringclean(n[:-1])+n[-1]

print(stringclean('cckwwweii'))

def countHi2(n):
    if len(n)<2:
        return 0
    if len(n)==2 and n[-1]=='i' and n[-2]=='h':
        return 1
    if n[-1]=='i' and n[-2]=='h' and n[-3]!='x':
        return 1+countHi2(n[:-1])
    else:
        return countHi2(n[:-1])

print(countHi2('hixhiahi'))

def parenBit(n):
    if n=='':
        return ''
    if n[0]!='(':
        return parenBit(n[1:])
    if n[-1]!=')':
        return parenBit(n[:-1])
    else:
        return n
    
print(parenBit('chen(ke)wei'))

def nextparen(n):
    if n=='':
        return True
    if n[0]=='(' and n[-1]==')':
        return nextparen(n[1:-1])
    else:
        return False
    
print(nextparen('(()))'))

def strCount(n,sub):
    if len(n) < len(sub):
        return 0
    if n[0:len(sub)]==sub:
        return 1+strCount(n[1:],sub)
    else:
        return strCount(n[1:],sub)

print(strCount('ckwwwwwckw','ckw'))

def strCopies(n,sub,count):
    if len(n) < len(sub):
        if count==0:
            return True
        else:
            return False
    if n[0:len(sub)]==sub:
        return strCopies(n[1:],sub,count-1)
    else:
        return strCopies(n[1:],sub,count)

print(strCopies('ckwwwwckw','ckw',2))
    
def strDist(n,sub):
    
    
    if n[-len(sub):] != sub:
        return strDist(n[:-1], sub)
    if n[0:len(sub)] != sub:
        return strDist(n[1:], sub)
    else:
        return len(n)

print(strDist('cckwwwwckwei','ckw'))





    
