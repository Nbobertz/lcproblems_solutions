"""
This is longest sub special cahr
"""


class Solution:
    def maximumLength(self, s: str) -> int:
        def is_special(sub):
            return len(set(sub)) == 1

        max_l = -1
        hm = defaultdict(int)

        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                subs = s[i:j]
                if is_special(subs):
                    hm[subs]+=1

        for x,y in hm.items():
            if y >= 3:
                print(len(x))
                max_l = max(max_l,len(x))
        return max_l

