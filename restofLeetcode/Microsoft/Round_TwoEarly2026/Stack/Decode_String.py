"""
This is for decoding a string, the trick is to pop from the right to left and then multiply by integers
"""


class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return None

        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                # build substring
                tmp = ''
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp
                # pop one to go back
                stack.pop()

                # build the num to multiply by
                num = ''
                while stack and stack[-1].isdigit() == True:
                    num = stack[-1] + num
                    stack.pop()
                stack.append(tmp * int(num))
        return ''.join(stack)

