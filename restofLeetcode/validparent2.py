#we are going to do valid parenthesis again to warm up.

#below is input and function
s = "]"

def solution(s):
    #first we turn the s string into a list
    s = list(s)

    #below we create the stack. The idea is that we create a hashmap with the key as the negative value and the value as the current value.
    stack =[]
    hmap ={')':'(',']':'[','}':'{'}

    #now we go through the s list left to right. If the bracket is open we add it to the stack at -1 and if we encounter a closed bracket we check to see that the stack[-1] matches it. if not we return False, if it does we return True. If at the end the len of stack is ==0 then we return True

    for char in s:
        if char in hmap:
            if len(stack)!=0 and stack[-1]==hmap[char]:
                stack.pop()
            else:
                answer = False
                return answer
        else:
            stack.append(char)


    if len(stack)==0:
        answer = True
        return answer
    else:
        answer = False
        return answer


print(solution(s))