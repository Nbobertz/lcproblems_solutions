"""
This problem stumped me so I had to get some help. I was on the right path but got held up. This is leetocde 3090 max len substring


"""

class Solution(object):
    def maximumLengthSubstring(self, s):
        hm = {}
        answer = 0

        l, r = 0, 0

        while r < len(s):
            # add s[r] to hashmap
            if s[r] not in hm:
                hm[s[r]] = 1
            else:
                hm[s[r]] += 1

            # shrink window while invalid (any char > 2)
            while hm[s[r]] > 2:
                hm[s[l]] -= 1
                l += 1

            # update max length
            delta = r - l + 1
            answer = max(answer, delta)

            r += 1  # move right pointer

        return answer