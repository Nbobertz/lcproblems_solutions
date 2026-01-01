"""
This is a subarray problme where we find all sub arrays
"""

count = 0
prefix_sum = 0
seen = {0: 1}  # prefix sum 0 occurs once

for num in nums:
    prefix_sum += num

    if prefix_sum - k in seen:
        count += seen[prefix_sum - k]

    seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

return count