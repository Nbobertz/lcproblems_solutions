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

class Solution(object):
    def isValid(self, s):
        if len(s) < 3:
            return False

        stack = []
        for c in s:
            stack.append(c)
            if len(stack)>=3:
                if stack[-1] == 'c' and stack[-2] == 'b' and stack[-3] == 'a':
                    stack.pop()
                    stack.pop()
                    stack.pop()
        if len(stack) == 0:
            return True
        elif len(stack) > 0:
            return False