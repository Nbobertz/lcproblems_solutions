"""
Pretty simple we aer just using a stack to solve this
"""


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # so this is a stack problem o(n) time and space

        ans = 0
        if not operations:
            return ans

        stack = []

        for o in operations:

            # adds int to stack
            if o.isdigit() == True or o[0] == '-':
                stack.append(int(o))

            else:
                if o == '+':
                    stack.append((stack[-1] + stack[-2]))
                elif o == 'D':
                    stack.append((stack[-1] * 2))
                elif o == 'C':
                    stack.pop()

        for n in stack:
            ans += n

        return ans