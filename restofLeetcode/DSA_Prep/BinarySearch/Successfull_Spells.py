"""
This was a binary search problem that I just did not get in time.


"""

answer = []

#this was my o(n2) pass that worked but was not optimol
# #do two pointer pass 0(n2)
# for spell in spells:
#     cnt = 0
#     for pot in potions:
#         if spell * pot >= success:
#             cnt+=1
#     answer.append(cnt)

# return answer

answer = []
potions.sort()
n = len(potions)

for spell in spells:
    l, r = 0, n - 1
    idx = n  # default: if no potion works, index stays at n

    while l <= r:
        mid = (l + r) // 2
        if potions[mid] * spell >= success:
            idx = mid  # possible valid potion found
            r = mid - 1  # try to find smaller index
        else:
            l = mid + 1  # need a stronger potion

    # all potions from idx onward are successful
    answer.append(n - idx)

return answer