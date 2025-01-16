#here we are given an array and it is our goal to figure out which number does not appear twich; al lother numbers appear twice

nums = [2,2,1]

def solution1():
    appear = {}

    for x in nums:
        if x not in appear:
            appear[x]=1
        elif x in appear:
            appear[x]+=1

    for x in appear:
        if appear[x]!=2:
            return x


def bitwise():
    a = 0
    for i in nums:
        a ^= i
    return a


print(solution1())