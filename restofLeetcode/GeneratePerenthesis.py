#here we are going to be given an input integer. The idea is that this integer represents how many parenthesis you have to output. For example the integer 3 means you have to create all examples of parenthesis with this integer.

n = 3


#the solution here is to recursivly call a function within a function. We first create a stack and result array. The idea is that we will only add open parenthesis and then closed parenthesis based off the n value.

def solution():
    stack = []
    res = []

    def backtrack(openN,closedN):
        if openN==closedN==n:
            res.append(''.join(stack))
            return res

        if openN<n:
            stack.append('(')
            backtrack(openN+1,closedN)
            stack.pop()

        if closedN < openN:
            stack.append(')')
            backtrack(openN,closedN+1)
            stack.pop()

    backtrack(0,0)
    return res

print(solution())