"""
The idea here is that we have two stacks and need to figure out if both are the same after deleting characters


"""

class Solution(object):
    def backspaceCompare(self, s, t):
        #this is a stack problem we can simply create two stacks and if we see a # we pop from the top of the stack. If both stacks are == at the end then we can return True

        stack1 = []
        stack2 = []

        for char in s:
            if char != '#':
                stack1.append(char)
            elif stack1 and char == '#':
                stack1.pop()

        for char in t:
            if char != '#':
                stack2.append(char)
            elif stack2 and char == '#':
                stack2.pop()

        s = ''.join(stack1)
        t = ''.join(stack2)

        #logic to check to see if stack 1 and stack 2 == return True
        if s == t:
            return True
        elif s!= t:
            return False
