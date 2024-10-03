#Here we are going to be givne an array of 0's and 1's it is our job to loop through the array and figure out how many consecutive 1's there are. For example 0,1,1,1,0 would return the integer 3

#this is a stack question

nums = [1,1,0,1,1,1]

def solution():
    stack = []
    max1s=0
    for p1 in range(0,len(nums)):
        if nums[p1]==1:
            stack.append(1)
            max1s=max(len(stack),max1s)
        if nums[p1]==0:
            stack=[]
    return max1s

answer = solution()
print(answer)
