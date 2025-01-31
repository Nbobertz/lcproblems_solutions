#here we are given an input array of integers 0,2,4,8. The array can look like [2,4,0,8] and the idea is that we need to merge similar elements together and replace that position with the integer.
#only similar numbers can smash into each other so [2,2,0,0] would end up [4,0,0,0] also integers can 'transcend' 0's. So all 0's must be in place.

nums = [8,0,4,4]
nums2 = [8,8,8,8]
nums3 = [2,0,0,2]
nums4 = [2,4,4,8]

def solution(x):
    arr = x

    #build two array's, a 0 and a stack. The idea here is that we will peek top of the stack to see if it's ismliar. If it is then we combine and then insert into location.

    #const vars
    answer = []
    zeros = []
    stack = []

    #now we loop through and see if we can catch
    for x in arr[::-1]:
        if x == 0:
            zeros.append(x)
        elif x!=0:
            if len(stack)==0:
                stack.append(x)
            else:
                if stack[-1]==8 and x == 8:
                    stack.pop()
                    stack.append(6)
                    stack.append(1)
                elif stack[-1]==x:
                    tmp = x + stack.pop()
                    stack.append(tmp)
                    zeros.append(0)


                elif stack[-1]!=x:
                    stack.append(x)
    answer = [x for x in stack[::-1]]
    answer = answer + zeros
    print(answer)
solution(nums4)
