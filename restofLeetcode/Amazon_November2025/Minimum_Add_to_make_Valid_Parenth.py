"""
Minimum to add to make the parenthesis valid


"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        hm = {
            '}':'{',
            ')':'(',
            ']':'['
        }

        stack = []
        broke = []

        count = 0
        for p1 in range(0,len(s)):
            char = s[p1]
            if char not in hm:
                #it is open
                stack.append(char)
            elif char in hm:
                if stack and hm[char] == stack[-1]:
                    stack.pop()
                elif stack and hm[char] != stack[-1]:
                    broke.append(char)
                else:
                    broke.append(char)

        answer = len(broke) + len(stack)
        return answer