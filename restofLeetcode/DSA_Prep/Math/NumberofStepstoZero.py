"""
This is just a recursion loop to find out how many times it takes to get to zero
"""

class Solution(object):
    def numberOfSteps(self, num):
        steps = 0
        while num != 0:
            if num%2 == 0:
                #it's even
                steps+=1
                num = num//2
            elif num%2 != 0:
                #it's odd
                steps += 1
                num -=1
        return steps