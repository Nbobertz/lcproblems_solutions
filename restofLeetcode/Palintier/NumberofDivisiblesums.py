#here we are going to be given an array and an integer. We need to see how many divisible sums there are where the d variable is module to 0 on the triplet
import collections

nums = [3,3,4,7,8]
d = 5


def solution():
    #capture len of nums
    n = len(nums)
    aux = collections.defaultdict(list)#create a default dict

    #now we loop through and get a remainder key
    for i in range(n-1): #leave room for next for loop
        for j in range(i+1,n):
            key = (nums[i]+nums[j])%d
            aux[key].append((i,j))

    #now we take what we stored and add k and then module against it to see if the remainder is 0
    res = 0
    for k in range(2,n):
        cur = nums[k]%d
        require = (d-cur)%d
        res += sum(1 for (i,j) in aux.get(require,[])if j<k)

    return res

print(solution)