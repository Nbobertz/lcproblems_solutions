"""
Here we just want to sort colors. Since the array only contains 0,1,2 we can had code those
"""

hm = {}
nn = len(nums)
for i,n in enumerate(nums):
    if n not in hm:
        hm[n] = 1
    elif n in hm:
        hm[n] += 1

if 0 in hm:
    for x in range(hm[0]):
        nums.append(0)
        nums.pop(0)
if 1 in hm:
    for x in range(hm[1]):
        nums.append(1)
        nums.pop(0)
if 2 in hm:
    for x in range(hm[2]):
        nums.append(2)
        nums.pop(0)