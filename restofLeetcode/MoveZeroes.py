#here we are going to be given an array of integers including zeros. The idea is that we will move all zeroes to the right of hte array while mainting the relative order of the array.

#the easiest solution here is to simply use a stack and loop through the array. If we hit a 0 then we append to stack and pop index out of array. Once we hit the end we append to nums array until all zeroes are out of the stack.

nums = [0,1,0,3,12]


def solution():
    stack = []

    for x in nums:
        if x == 0:
            stack.append(x)
            nums.remove(x)
    for x in stack:
        nums.append(x)

    stack=[]

    for x in nums:
        if x == 0:
            stack.append(x)
            nums.remove(x)
    for x in stack:
        nums.append(x)

#not the most optimal solution here is the two pointer approach

def solution2():
    left = 0

    for right in range(len(nums)):
        if nums[right]!=0:
            nums[right],nums[left] = nums[left],nums[right]
            left +=1

solution2()
print(nums)