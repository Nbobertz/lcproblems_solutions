#here we are redoing the valid parenthesis question. The idea is that we will be given a string of proper parenthesis [,(,),],{,} characters and we have to return true if it is valid and false if not.

#example
s = "()[]{}"

def solution():
    stack = []

    #purpose of hashmap is to assign value to each individual key of what we could encounter in the stack
    matchinghashmap={'}':'{',']':'[',')':'('}

    for char in s:
        if char in matchinghashmap:
            if stack and stack[-1]==matchinghashmap[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    if len(stack)!=0:
        answer = False
    else:
        answer = True

    return answer

print(solution())