"""
The idea is that we have a singular stack and as you iterate through the array and append all characters to the stack.
If you hit a digit then simply pop from the stakc
"""


class Solution(object):
    def clearDigits(self, s):
        # iterate backwards
        stack = []

        for char in s:
            if char.isdigit() == False:
                stack.append(char)
            elif char.isdigit() == True:
                stack.pop()

        # join the stack
        answer = ''.join(stack)
        return answer