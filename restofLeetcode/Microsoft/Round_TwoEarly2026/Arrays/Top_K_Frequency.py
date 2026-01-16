"""
Top k frequent bucket sorts
"""

# this is a bucket sort
# buc = [[1],[2],[3],[],[],[]]

answer = []

if not nums:
    return []

# build the map #o(n)
hm = {}
for n in nums:
    if n not in hm:
        hm[n] = 1
    elif n in hm:
        hm[n] += 1

# construct bucket array o(n)
buc = []
for _ in range(len(nums) + 1):
    buc.append([])

# read from the array and append freq of hm to index of buc
for n, i in hm.items():
    buc[i].append(n)

count = 0
# o(n2)
for b in buc[::-1]:
    if len(b) != 0 and count < k:
        # found an integer in bucket
        for n in b:
            answer.append(n)
            count += 1
return answer