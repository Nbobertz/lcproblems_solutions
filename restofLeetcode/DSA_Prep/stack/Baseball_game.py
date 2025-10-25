"""
The idea here is that we have to keep track of baseball game values as we see them. This is a stack problem and I solved it with optimal space and time complexity


"""


class Solution(object):
    def calPoints(self, operations):
        stack = []

        record = 0

        for p1 in range(0, len(operations)):
            op = operations[p1]
            if op != '+' and op != 'D' and op != 'C':
                # we have number
                stack.append(int(op))

            # now logic on stack
            if op == '+':
                if len(stack) < 2:
                    # we have af aulty lineup
                    return False

                elif len(stack) >= 2:
                    print(stack)
                    # sum up previous 2 seen integers
                    n1 = stack[-1]
                    n2 = stack[-2]
                    n3 = n1 + n2
                    stack.append(n3)

            elif op == 'D':
                if len(stack) == 0:
                    # don't have score to capture
                    return False

                elif len(stack) > 0:
                    n1 = stack[-1]
                    n2 = int(n1) * 2
                    stack.append(n2)
                    print(stack)

            elif op == 'C':
                if len(stack) == 0:
                    # nothing to invalidate
                    return False

                elif len(stack) != 0:
                    stack.pop()

        record = sum(stack)

        return record

