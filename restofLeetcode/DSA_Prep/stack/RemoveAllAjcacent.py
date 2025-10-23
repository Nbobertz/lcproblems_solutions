"""
The idea here is that we remove all adjacent characters from a string and then return it


"""

class Solution(object):
    def removeDuplicates(self, s):
        #this is a stack problem because we are going to go left to right and then eliminate if we see the same at [-1] and 0

        stack = []

        for char in s:
            #check to see if char in stack at -1
            if stack and char == stack[-1]:
                stack.pop()
            elif len(stack) == 0 or char != stack[-1]:
                #either nothing in stack or does not equal -1
                stack.append(char)

        #now we should be able to return stack
        answer = ''.join(stack)
        return answer