"""
Redid the parenthesis problem

"""

class Solution:
    def isValid(self, s: str) -> bool:
        #so we can use a stack for this. The idae is tha keep track of the opening parenths we see
        #then we simply close them as we see them

        #first we need to catch edge cases
        if not s or len(s) == 0:
            return False
        if len(s) % 2 != 0:
            #we have an odd amount, automatic false
            return False

        stack = []
        stack.append(s[0])

        hm = {
            ']':'[',
            '}':'{',
            ')':'('
        }

        for char in s[1:]:
            if char not in hm:
                stack.append(char)
            if char in hm:
                if stack and stack[-1] != hm[char]:
                    return False
                elif stack and stack[-1] == hm[char]:
                    stack.pop()

        print(stack)
        if len(stack) == 0:
            return True
        elif len(stack)!=0:
            return False