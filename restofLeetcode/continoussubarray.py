#here we are given an integer array. We have to figure out how may subconinous arrays there are. A subarray is continous if it's range is not more than 2


nums = [5,4,2,4]

def solution():
    # Map to maintain sorted frequency map of current window
    freq = {}

    # initilze left and right pointer at 0 for window
    left, right = 0, 0

    # keep track of valid subarrays
    count = 0  # Total count of valid subarrays

    while right < len(nums):
        # Add current element to frequency map
        freq[nums[right]] = freq.get(nums[right], 0) + 1

        # While window violates the condition |nums[i] - nums[j]| ≤ 2
        # Shrink window from left
        while max(freq) - min(freq) > 2:
            # Remove leftmost element from frequency map
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1

        # Add count of all valid subarrays ending at right
        count += right - left + 1
        right += 1

    return count

print(solution())