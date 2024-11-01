#here we are going to be given a string and we have to delete characters in the string so that no three consecutive characters are the same.

s = "aab"

def solution():
    # sliding window: couldn't get it to work properly. Need to practice SW
    l, r = 0, 1
    answer = ''

    while r < len(s):
        answer += s[l]
        if s[l] == s[r]:
            if s[r+1]!=None and s[r+1]==s[l]:
                while r + 1 < len(s) and s[l] == s[r + 1]:
                    r += 1
                l = r
                r+=1
            else:
                r+=1
                answer += s[r]
        else:
            l+=1
            r+=1
    answer += s[-1]

    return answer

def solution2():
    #using stack
    stack = []
    answer = ''

    for char in s:
        if len(stack)<2:
            answer+=char
            stack.append(char)
        elif char == stack[-1] and char==stack[-2]:
            stack.append(char)
        elif char!=stack[-1]:
            stack.append(char)
            answer+=char
        elif char==stack[-1] and char!=stack[-2]:
            stack.append(char)
            answer+=char
    return answer

print(solution2())