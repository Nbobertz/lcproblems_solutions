#here is one of Google's most common problems; two sum.

nums=[2,7,11,15]
target = 9




#below is On2 approach
def solution():
    hm = {}

    for index,num in enumerate(nums):
        if target - num in hm:
            return [index,hm[target-num]]
        hm[num]=index



def solution2():
    for p1 in range(0,len(nums)):
        for p2 in range(p1+1,len(nums)):
            if nums[p1]+nums[p2]==target:
                return p1,p2
print(solution())