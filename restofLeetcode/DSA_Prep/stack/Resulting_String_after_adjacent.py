"""
This is just to convert the characters to ord and then use the number to add/remove characters from stack.

"""

class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and (abs(ord(stack[-1]) - ord(c)) == 1 or abs(ord(stack[-1]) - ord(c)) == 25):
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)