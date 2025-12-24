"""
This is just keeping track of scores using a stack
"""


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        answer = 0
        if not operations:
            return answer

        stack = []

        for x in operations:
            if x[0] == '-':
                x2 = x[1:]
                if x2.isdigit() == True:
                    x2 = int(x2) * -1
                    stack.append(int(x2))
            elif x.isdigit() == True:
                stack.append(int(x))
            elif x == '+':
                n1, n2 = stack[-1], stack[-2]
                n3 = n1 + n2
                stack.append(n3)
            elif x == 'D':
                n1 = stack[-1]
                stack.append(n1 * 2)
            elif x == 'C':
                stack.pop()
        return sum(stack)