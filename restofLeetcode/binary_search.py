#we are going to do the classic binary search problem. This is a leetcode easy and is just to test to see if you know the binary search algorithm.

#you are going to be given an array of integers (nums) which is pre-sorted in ascending order. Further, you will be given a variable of target which is a number. If the number is in the array nums you will return the index point or else if it is not return -1.

#so the trick here is that the array is pre-sroted in ascending order when you get it. So nums = 1,2,3,4,5,6 and let's say the target is 3. You could loop through the array until you find 3 but the problem is what happens if hte array len is 10 million? You going to loop 10 million times? No the best way to do this is to use binary search which is to half the point each time. So for the array 1,2,3,4,5,6 just start at 3 if it's higher or lower move the pointer.

nums = [-1,0,3,5,9,12]
target = 5

def solution():
    l,r =0,len(nums)-1
    answer = -1
    while l<=r:
        halfpoint = int((l+r)/2)
        if target<nums[halfpoint]:
            r = halfpoint-1
        if target>nums[halfpoint]:
            l = halfpoint+1
        if nums[halfpoint]==target:
            answer = halfpoint
            return answer
    return answer


#did this one first try in under 20 min
#the idea here is that you half the distance between l and r. Then run the logic based off that
print(solution())