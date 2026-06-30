"""
This is a monotonic stack problem. A classic one that I think is a great problem
Got it first try
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
                #this is a monotonoic stack. Lets see if I can do it first try

        ans = []
        if not temperatures:
            return ans

        #stores placeholders
        for n in range(len(temperatures)):
            ans.append(0)

        stack = []

        for i,n in enumerate(temperatures):
            if not stack:
                stack.append((i,n))
            else:
                while stack and n > stack[-1][-1]:
                    ind,temp = stack.pop()
                    ans[ind] = i-ind
                stack.append((i,n))
        return ans