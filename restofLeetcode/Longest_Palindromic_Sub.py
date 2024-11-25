#here we are going to be given a string and our goal is to return the longest sub-palindromic string. So babad would be 'bab' or 'aba'

# I think the easiest way to go about this would be to do two pointer. First pointer at 0 index and second pointer at -1. We go from -1 to p1+1 to see if palindrom exists. If so we add to stack and at the end pull the 'largest'

s = "babad"

def solution():
    stack = ['']

    for p1 in range(0, len(s)):
        counter=0
        for p2 in range(p1,len(s)):
            counter-=1
            place = len(s)+counter+1
            front=s[p1:place]
            backr = reversed(front)
            back=''.join(backr)
            if front==back and len(front)>=len(stack[-1]):
                stack.append(front)
    return stack[-1]


print(solution())