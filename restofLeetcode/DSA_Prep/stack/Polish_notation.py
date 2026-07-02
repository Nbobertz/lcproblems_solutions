"""
This one needs to be watched out for. Here there are several gotchas
Such as rounding to zero and navigating the concept of a 3 digit negative number
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []

        for o in tokens:
            # Check if the token is an integer (positive or negative)
            if o.lstrip('-').isdigit():
                stack.append(int(o))
            else:
                i1 = stack.pop()
                i2 = stack.pop()

                if o == '+':
                    stack.append(i2 + i1)
                elif o == '-':
                    stack.append(i2 - i1)
                elif o == '*':
                    stack.append(i2 * i1)
                elif o == '/':
                    # Truncate toward zero
                    stack.append(int(i2 / i1))

        return stack[-1]