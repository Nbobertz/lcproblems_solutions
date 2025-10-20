"""
Easy problem for just removing stars from a string. We use a stack


"""

class Solution(object):
    def removeStars(self, s):
        #this is a stack problem and can be done in o(n). Much like valid parenthesis

        stack = []

        for char in s:
            if char != '*':
                stack.append(char)
            elif char == '*':
                stack.pop()
        #turn stack into string
        answer = ''.join(stack)
        return answer