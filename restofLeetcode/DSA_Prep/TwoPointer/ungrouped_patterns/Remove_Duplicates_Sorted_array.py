"""
Remove duplicates from sorted array
"""

seen = set()
write = 0

for x in nums:
    if x not in seen:
        seen.add(x)
        nums[write] = x
        write += 1

return write