def binarysearch(List,number):
    found=0
    Searchfailed=0
    first=1
    last=len(List)
    while found==0 and Searchfailed==0:
        mid=(first+last)//2
        if List[mid]==number:
            found=1
        else:
            if first>=last:
                Searchfailed=1
            else:
                if List[mid]>number:
                    last=mid-1
                else:
                    first=mid+1
    if found==1:
        return mid+1
    else:
        return 'not found'
                
