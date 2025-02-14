#here we are given an array of integers and it is our goal to try and find out if one is divislbe by another module integer
import collections

nums = [3,3,4,7,8]
d = 5

def solution():
    #capture len of nums
    #init a dictionary-default dict

    n = len(nums)
    hm = collections.defaultdict(list)

    #first for loop get module division of first two
    for i in range(n-1):
        for j in range(i+1,n):
            key = (nums[i]+nums[j])%d #gets number divisible
            hm[key].append((i,j))


    #create result in
    res = 0

    #now loop through a third time and get the third number
    for k in range(2,n):
        cur = nums[k]%d
        req = (d-cur)%d #get the current module division and minus the cur to figure out what we are missing
        for i,j in hm.get(req,[]):
            if j<k:
                res+=1

    return res


print(solution())