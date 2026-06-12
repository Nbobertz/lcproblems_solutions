"""
you can do sorting here or simple ord the characters

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # this is a sorting problem that I think we can do with a sort and then return the same
        # first sort
        ans = []
        if not strs:
            return ans

        tmp = []
        for i, w in enumerate(strs):
            w = list(w)
            w.sort()
            w = ''.join(w)
            tmp.append((w, i))

        # create a map of frequencies
        hm = {}
        for x, i in tmp:
            if x not in hm:
                hm[x] = [i]
            elif x in hm:
                hm[x].append(i)

        # now read from map and group
        for x in hm:
            tt = []
            for i in hm[x]:
                tt.append(strs[i])
            ans.append(tt)

        return ans