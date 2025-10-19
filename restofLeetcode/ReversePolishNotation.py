#here we are going to be given an array of strings. Each sting is gong to be either a number or an mathmatical operation (+,-,*,/). This string of characters is going to be in reverse polish notation (RPN). The goal here is to return the value of the exppression. The expression is always valid so no dividing by 0 or anything crazy.

#this problem tests to see if you know what RPN is and how to calculte it along with your concept of a stack.

#Reverse polish notation is where you read a series of integers or operatiors from left to right. The integers are stored to memory and when you hit an operator you then perform the operation on those two integers.

#for example [2,1,+,3,*] would equal out to 9: This is because we first take the 2 and 1 integers in the 0,1 index point. After this see at index point 2 there is a '+' sign. This tells us to add the 2 and 1 together. Now the memory stored is 3. Our array is now [3,3,*] and as you might expect you would take your 3 and 3 and multiply it.

#the problem will only feature whole numbers and you will have to truncate towards 0.

#this problem is the same as valid parenthesis if you know that one. below is the example and solution.

tokens= ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]


def solution():
    sstack = []
    operats = ['+','/','*','-']
    for p1 in range(0,len(tokens)):
        #to lazy to type the tokens[p1
        char = tokens[p1]
        if char not in operats:
            sstack.append(int(char))
        else:
            if char == '+':
                tmpnum = sstack[-2]+sstack[-1]
                sstack.pop()
                sstack.pop()
                sstack.append(tmpnum)
            if char == '-':
                tmpnum = sstack[-2]-sstack[-1]
                sstack.pop()
                sstack.pop()
                sstack.append(tmpnum)
            if char == '/':
                tmpnum = sstack[-2]/sstack[-1]
                sstack.pop()
                sstack.pop()
                sstack.append(tmpnum)
            if char == '*':
                tmpnum = sstack[-2]*sstack[-1]
                sstack.pop()
                sstack.pop()
                sstack.append(tmpnum)
    answer = int(sstack[0])
    return answer


#problem came up with an edge case. DSA_Prep's solution solved it. I think the problem came down to me appending to the other stack wrong.
def solution2():
    stack = []
    for c in tokens:
        if c =='+':
            stack.append(stack.pop()+stack.pop())
        elif c == '-':
            a,b = stack.pop(),stack.pop()
            stack.append(b-a)
        elif c == '*':
            stack.append(stack.pop() * stack.pop())
        elif c == '/':
            a,b = stack.pop(), stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(c))
    return stack[0]

answer = solution2()
print(answer)
