#the goal here is to find the maximum product from an array. This is a dynamic programing problem and requires you to store both the positive and negative numbers as you loop through the array.

#below is a test example
nums = [2,3,-2,4]
#highest subarray product in the above test is 6 (2*3)

#below is the neetcode solution
def solution():
    res = max(nums)
    curmimn,curmax = 1,1

    for n in nums:
        if n==0:
            curmimn=1
            curmax=1
            continue
        else:
            tmp = curmax*n
            curmax = max(n*curmax,n*curmimn,n)
            curmimn = min(tmp,n*curmimn,n)
            res = max(res,curmax,curmimn)
    return res


print(solution())