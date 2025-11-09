"""
if num is even divide in half if it's odd just sub by one. Return steps needed to get num to zero
"""

class Solution(object):
    def numberOfSteps(self, num):
        answer = 0
        #just use % to see if odd until 0
        while num > 0:
            #is it odd or even?
            if num % 2 == 0:
                #even
                num = num//2
            else:
                num-=1
            answer+=1
        return answer