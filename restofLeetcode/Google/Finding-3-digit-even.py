#here we are going to be given an input array and then we have to go through this array and return a sorted array of integers whic hcan be cobined into 3 diffrent uniqu integers and is even
#has to no have any leading zeros
import itertools

digits = [1,0,2,3,4,6]



def solution():
    ans = set()
    for x,y,z in itertools.permutations(digits,3):
        if x!= 0 and z & 1 == 0:
            tmp = 100*x + 10*y +z
            ans.add(tmp)
    return sorted(ans)

print(solution())