"""
This is supposed to be a stack problem but you can simply continously remove "abc" from the word until
it is either a len of 0 or none and it passes
"""

class Solution(object):
    def isValid(self, s):
        while "abc" in s:
            s = s.replace("abc","")
        if len(s) == 0:
            return True
        elif len(s) != 0:
            return False