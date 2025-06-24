#here we are given an array and told to return True of the array contains any dupilcate integers

nums = [1,2,3,3,4,5,6] #there are two 3's should return true
nums2 = [1,2,3,4,5,6,7] #no dupicates, should return False

def solution(nums):
    #this is a hashmap solution. We can itearate using two pointer p1 = 0 index and p2 = p1 +1. But this is going to be O(2) and not that efficent
    hm = {} #const hashmap

    for n in nums:
        if n in hm:
            return True
        elif n not in hm:
            hm[n]=1

    return False


answer = solution(nums)
print(answer)
