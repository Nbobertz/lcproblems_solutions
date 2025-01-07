#here we are going to take an input integer and then generate the maximum number of valid parenthesis for that number of valid parenthesis.

n = 3

def solution():
    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append(''.join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res

print(solution())