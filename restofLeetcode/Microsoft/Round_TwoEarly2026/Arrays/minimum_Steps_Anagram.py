"""
This is the minimum number of steps needed to take to make something an anagram
"""


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        steps = 0
        if not s:
            return steps

        elif not t and len(s) > 0:
            return steps

        hm = {}

        # build the frequency map
        for char in s:
            if char not in hm:
                hm[char] = 1
            elif char in hm:
                hm[char] += 1

        new_char = 0
        nc = []
        for char in t:
            if char not in hm:
                # found a new character
                new_char += 1
                nc.append(char)
            elif char in hm:
                hm[char] -= 1

        # loop through hashmap and add to steps then add new char
        for key, value in hm.items():
            if str(value)[0] == '-':
                # found negative
                new_char += abs(value)

        return new_char