#the goal here is to find the square root of a given integer. We will also have to round down. You can't use any built in functions to find this number. There will always be a number and you have to round down. The square root of a number is a number that when multiplied by itself equals the target.

#below is the test case
x = 36222222

#below is the solution I came up with not very efficent and it brute forces stuff.
def solution():
    answer = 0
    if x <2:
        answer = x
        return answer
    if x == 2:
        answer = 1
        return answer
    for p1 in range(0,x):
        if p1*p1==x:
            answer = p1
            return answer
        elif p1*p1>x:
            answer = p1-1
            return answer



#below is the binary search option. Here we cut the results in half and then take the middle and square it. If the result is greater than the target number (x) we will then move the right pointer -1 if it is less then we will move the left pointer +1 (moving hands to center)
def solution2():
    l,r = 0,x
    result = 0

    while l<=r:
        middle = l+((r-l)//2)
        if middle**2>x:
            r=middle-1
        elif middle**2<x:
            l=middle+1
            result=middle
        else:
            return middle
    return result


print(solution2())