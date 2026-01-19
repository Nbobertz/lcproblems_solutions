"""
Here we want to grab all substrings possible by expanding aroudn {} quotes
"""

class Solution:
    def expand(self, s: str) -> List[str]:
        s = s.replace("{",' ').replace('}',' ').split()
        res = []

        def dfs(i,w):
            if i == len(s):
                res.append(w)
                return
            for a in s[i].split(','):
                dfs(i+1,w+a)
        dfs(0,'')
        res.sort()
        return res