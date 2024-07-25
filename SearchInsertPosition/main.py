#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#below is test case
nums = [1,3,5,6]
target = 7


#create the setup algorithm
def solution():
    for x in range(0,len(nums)):
        if nums[x]==target:
            answer = x
            return answer
        elif nums[x]>target:
            answer = x
            return answer
        if x == len(nums)-1:
            answer = x+1
            return answer

answer = solution()
print(answer)