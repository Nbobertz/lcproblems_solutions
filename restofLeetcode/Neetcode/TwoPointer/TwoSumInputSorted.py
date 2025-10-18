"""
The idea here is taht we have to use math to move pointers as we see them if its above or below what the target is


"""

n = len(numbers)
l, r = 0, n - 1

# while loop to capture to see if it equals up to target
while l < r:
    # move pointers based off math
    if numbers[l] + numbers[r] > target:
        # move r pointer to the left
        r -= 1
    elif numbers[l] + numbers[r] < target:
        l += 1
    elif numbers[l] + numbers[r] == target:
        return [l + 1, r + 1]