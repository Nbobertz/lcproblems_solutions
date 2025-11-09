"""
Just count the number of operations until we get to zero
"""

class Solution(object):
    def countOperations(self, num1, num2):
        answer = 0

        #what if no number1/2 or one is == 0
        if not num1 or not num2 or num1 == 0 or num2 == 0:
            return answer

        while num1 > 0 or num2 > 0:
            #logic
            if num1 >= num2:
                num1 = num1-num2
            elif num2 > num1:
                num2 = num2-num1
            answer+=1
            if num1 == 0 or num2 == 0:
                break
        return answer
