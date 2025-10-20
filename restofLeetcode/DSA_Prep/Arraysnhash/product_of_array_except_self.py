#here we are given an array and told that we need to find the product of the array (multiply) of all numbers except the index point at which we are at.

"""
For example, if the array [1,2,3,4] the answer would be [24,12,8,6]. This is because at each index point we would not multiply by the integer at that point but all other integers
"""

nums = [35,22,34,30,32]

def solution():
    # I think we can do this with two pointer pretty easy but it's not going to be O(N)

    answer = []

    for p1 in range(0, len(nums)):
        tmp = None
        for p2 in range(0, len(nums)):
            if p1 != p2:
                if tmp != None:
                    tmp = tmp * nums[p2]
                else:
                    tmp = nums[p2]

        answer.append(tmp)

    return answer

def efficent():
    n = len(nums)
    answer = [1] * n  # Step 1: Initialize result array with 1s

    # Step 2: Compute left products
    left = 1
    for i in range(n):
        answer[i] = left  # Product of all elements to the left of i
        left *= nums[i]  # Update left product for next index

    # Step 3: Compute right products and multiply
    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right  # Multiply by product of all elements to the right
        right *= nums[i]  # Update right product for next index

    return answer

print(solution())