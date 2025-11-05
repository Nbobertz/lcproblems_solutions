"""
Here the idea is that we have to find all anagrams in an array as we slid across it. We are given an array that we need to check against


"""


class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return res

        # frequency arrays for 'a' to 'z'
        p_count = [0] * 26
        window_count = [0] * 26

        # helper to map char -> index (0–25)
        def idx(c):
            return ord(c) - ord('a')

        # fill frequency for p
        for c in p:
            p_count[idx(c)] += 1

        for i in range(len_s):
            # add current char
            window_count[idx(s[i])] += 1

            # remove leftmost char if window > len_p
            if i >= len_p:
                window_count[idx(s[i - len_p])] -= 1

            # compare only after reaching window size
            if window_count == p_count:
                res.append(i - len_p + 1)

        return res
