#here we are given an array containing the integers 2,4,0,8 in random order. If two of the same integers land next to each other we will have to smash them together and put that number as the replacement

#move all 0's to the right side

#finally got it.

nums = [2,4,0,4,8,8,0,0,4,4,2]

#[8,8,2]
#[1,6,2]
#[1,6,2,0]

#[2,1,6,8]

def solution():

    #put into stack, count zeros, append at end

    #const vars
    zeros = []
    stack = []
    answer = []

    for x in nums:
        if x == 0:
            zeros.append(x)
        else:
            if len(stack) == 0:
                stack.append(x)
            elif x == 8 and stack[-1] == 8:
                stack.pop()
                stack.append(1)
                stack.append(6)
            else:
                if x == stack[-1]:
                    num = x+stack[-1]
                    stack.pop()
                    stack.append(num)
                else:
                    stack.append(x)


    #call while loop to move and pop from stack. Break if stack hit's 1
    while stack:
        l = 0
        if len(stack)==1:
            break
        if l<len(stack)-2 and stack[l]!=stack[l+1]:
            num = stack.pop(0)
            answer.append(num)
        elif l!=len(stack)-2 and stack[l]==stack[l+1]:
            if stack[l] == 8 and stack[l] == stack[-1]:
                stack.pop()
                stack.pop()
                answer.append(1)
                answer.append(6)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if num1 != num2:
                    answer.append(num1)
                    answer.append(num2)
                else:
                    tmpnum = num1+num2
                    answer.append(tmpnum)
        l+=1
    if answer[-1] == stack[0]:
        if answer[-1] == 8:
            answer.pop()
            answer.append(1)
            answer.append(6)
        else:
            num3 = stack.pop()
            num4 = answer.pop()
            answer.append(num3+num4)
    else:
        answer.append(stack[0])
    answer = answer+zeros

    diff = len(nums)-len(answer)
    for x in range(0,diff):
        answer.append(0)
    return answer




print(solution())