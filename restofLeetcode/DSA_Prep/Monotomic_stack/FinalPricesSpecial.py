"""
So I need to get gud at monotomic stacks so here I am doing them contionusly

"""

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # # answer = []
        # for p1 in range(0,len(prices)):
        #     answer.append(prices[p1])
        #     for p2 in range(p1+1,len(prices)):
        #         if prices[p1]>=prices[p2]:
        #             #found smaller
        #             answer[p1] = prices[p1]-prices[p2]
        #             break
        # return answer

        reslist = prices[:] #: is copy
        stack = []

        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                index = stack.pop(-1)
                reslist[index] = prices[index] - prices[i]
            stack.append(i)

        return reslist