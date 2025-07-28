#this is a classic two pointer problem. We are given an input array and have to print the index's that have their numbers add up to a target.

numbers = [2,7,11,15]
target = 9

def solution():
    l, r = 0, len(numbers) - 1

    while l <= r:
        if numbers[l] + numbers[r] < target:
            l += 1
        elif numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]