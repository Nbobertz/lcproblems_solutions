#Here we are going to be given an array called nums with random whole integers that can be both positive and negative. The array can be any length of numbers. A subarray is any continous amount of numbers. Ex. 4,3,2,1 can be 4,3 or 4,3,2 or 3,2,1.

#To brute force this you could easily just do two pointer and just calculate every possible combiation of subarrays and take the highest.

#below is test case
nums = [-2,1,-3,4,-1,2,1,-5,4]

#below was my solution; it was ok but failed one edge case. O(n2)
# def solution():
#     highestarray = 0
#     if len(nums)==1:
#         highestarray=nums[0]
#     else:
#         for p1 in range(0,len(nums)):
#             value = nums[p1]
#             for p2 in range(p1+1,len(nums)):
#                 value+=nums[p2]
#                 if value>highestarray:
#                     highestarray=value
#     return highestarray
# print(solution())


def solution2():
    maximumsubb = nums[0]
    currentsum=0
    for p1 in nums:
        if currentsum<0:
            currentsum=0
        currentsum+=p1
        if currentsum>maximumsubb:
            maximumsubb=currentsum
    return maximumsubb

print(solution2())