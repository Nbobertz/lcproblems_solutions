"""
I am in the airport of St.Louis doing leetcode. I did this problem and while I got on the board it was not optiomal time and space complexity. It did work however so that is good.
"""

class Solution(object):
    def smallestNumber(self, n):
        #we might be able to do this with bitwize but we can at least get to o(n) solution via converting to bit and then converting to string, then to array, then to set to see if len of arry is 1

        end = False
        answer = 0
        x = n
        while end == False:
            num = bin(x)
            ss = list(num)
            del ss[0:1]
            if '0' not in ss:
                answer = x
                end = True
            else:
                x+=1

        return answer
