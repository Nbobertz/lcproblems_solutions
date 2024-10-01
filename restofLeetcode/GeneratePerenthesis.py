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
#the reason why the above solution works vs the check if parenthesis is good is because the logic is built into the openN and closedN funciton calls. Essentially the above code for the example 3 is to say if 0=0=n the return the answer because both the openn and closed n are equal to the number of parenthesis.

#we start by adding a ( and then increasing hte counter of openN by one. Then if closed is ever lower we instantly add a closed one.
print(solution())