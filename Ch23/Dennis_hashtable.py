#S3C3 Dennis

hashtable=[]*10

def insert(key):
    index=hash(key)
    print('Checking',index)
    while not hashtable[index]==0:
        index=index+1
        if index>len[hashtable]:
            index=1
        print('Checking',index)
    hashtbale[index]=key

def find(searchkey): 
    index=hash(hashkey)
    print('Checking',index)
    while not hashtable[index]==searchkey and not hashtable[index]==0:
        index=index+1
        if index>len[hashtable]:
            index=0
            print('Checking',index)
    if not hashtablep[index]==0:
        return index

insert(23)
insert(11)
find(11)
find(23)
    
