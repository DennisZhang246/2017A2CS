def groupSum(start,nums,target):
    if target==0:
        return True
    if start==len(nums):
        return False

    return groupSum(start+1,nums,target-nums[start]) or groupSum(start+1,nums,target)

print(groupSum(0,[12,23,34,45,56],102))

def groupSum6(start,nums,target):
    if start==len(nums):
        return (target==0)
    if nums[start]==6:
        return groupSum6(start+1,nums,target-6)
    else:
        return groupSum6(start+1,nums,target-nums[start]) or groupSum6(start+1,nums,target)

print(groupSum6(0,[11,6,4,6],17))

def groupNoAdj(start,nums,target):
    if start>=len(nums):
        return (target==0)
  
    return groupNoAdj(start+2,nums,target-nums[start]) or groupNoAdj(start+1,nums,target)

print(groupNoAdj(0,[2,6,10,7],8))

def groupSum5(start,nums,target):
    if start>=len(nums):
        return (target==0)
    if nums[start]%5==0:
        if nums[start+1]!=1:
            return groupSum5(start+1,nums,target-nums[start])
        else:
            return groupSum5(start+2,nums,target-nums[start])
    else:
        return groupSum5(start+1,nums,target-nums[start]) or groupSum5(start+1,nums,target)

print(groupSum5(0,[2,5,1,10,1,7],16))

def groupSumClump(start,nums,target):
    if target==0:
        return True
    if start==len(nums):
        return False
    if start<len(nums)-1 and nums[start]==nums[start+1]:
        n=0
        for i in range(len(nums)-2):
            if nums[start]==nums[start+i+1]:
                n=n+1
        return groupSumClump(start+n,nums,target-n*nums[start]) or groupSumClump(start+n,nums,target)
    return groupSumClump(start+1,nums,target-nums[start]) or groupSumClump(start+1,nums,target)

print(groupSumClump(0,[1,3,4,5,5,5],15))

def splitarray(n):
    if start>=len[nums]:
        return False
    
