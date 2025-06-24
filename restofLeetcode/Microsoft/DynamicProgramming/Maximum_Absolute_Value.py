#here we are given the integer array nums and asked to return the largest absolute value of all subarrays.

nums = [1,-3,2,3,-4]

def solution():
    sum, minSum, maxSum = 0, 0, 0
    for num in nums:
        sum += num
        maxSum = max(maxSum, sum)
        minSum = min(minSum, sum)
    return abs(maxSum - minSum)