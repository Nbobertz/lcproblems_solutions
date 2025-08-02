class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}

        if len(s) != len(t):
            return False

        s = list(s)  # ['r','a',c','e','c','a','r,]
        t = list(t)  # ['c','a','r','r','a','c','e']

        for char in s:
            if char not in hm:
                hm[char] = 1
            elif char in hm:
                hm[char] += 1

        for char in t:
            if char not in hm:
                return False
            elif char in hm:
                hm[char] -= 1
                if hm[char] == 0:
                    hm.pop(char)

        if len(hm) == 0:
            return True
        else:
            return False