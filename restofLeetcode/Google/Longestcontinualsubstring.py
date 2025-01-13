import time

s = "abcabcbb"

def solution():
    # create charset to keep track of unique string. When we hit duplicate character we simply remove l pointer from that charset and continue. Return max charset.


    #the l pointer is popping from the left of the charset and we iterate it by one
    charset = set()
    l = 0
    res = 0

    for r in range(0, len(s)):
        while s[r] in charset:
            charset.remove(s[l])
            l += 1
        charset.add(s[r])
        res = max(res, r - l + 1)
    return res

print(solution())