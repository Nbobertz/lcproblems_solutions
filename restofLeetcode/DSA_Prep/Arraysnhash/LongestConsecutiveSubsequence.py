#find the lognest consecutive subsequence 1,2,3,4,5, that is only +1

def solution():
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start sequence from the beginning
        if num - 1 not in num_set:
            current = num
            streak = 1

            while current + 1 in num_set:
                current += 1
                streak += 1

            longest = max(longest, streak)
    return longest