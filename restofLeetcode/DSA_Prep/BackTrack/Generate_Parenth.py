"""
Here we want to generate parenthesis out of an integer n. The max amount of possible good parenthesis and then return it
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        if not n:
            return

        stack = []
        def dfs(oN,cN):
            #open n and closed n count

            if oN == cN and oN == n:
                #we have a good parenth array
                answer.append(''.join(stack))
                return

            #add open parenthesis and inc oN by 1
            if oN < n:
                stack.append('(')
                dfs(oN+1,cN)
                stack.pop()

            if cN < oN:
                stack.append(')')
                dfs(oN,cN+1)
                stack.pop()

        dfs(0,0)

        return answer