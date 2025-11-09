"""
Got this one first try in under 10 minutes. Pretty good! Just build a sliding window and increment.
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        answer = []

        hm = {}
        # keep track of all possible subs as we move across

        if len(s) <= 10:
            return answer

        # can't look at DNA less then 10
        l, r = 0, 10

        # instantly put in hm
        s1 = s[l:r]
        hm[s1] = 1
        while r != len(s):
            l += 1
            r += 1

            # check to see if in hm
            tmp = s[l:r]
            if tmp in hm:
                hm[tmp] += 1
            elif tmp not in hm:
                hm[tmp] = 1

        # call frequencies and append anything greater then 1
        for dna, freq in hm.items():
            if freq > 1:
                answer.append(dna)

        return answer