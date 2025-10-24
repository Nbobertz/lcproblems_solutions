"""
Here we are given a string and have to remove all instances of a substring within it from the left most side.
This is a classic stack problem
"""

# this is a stack problem, append to stack and remove if it makes abc or whatever part is
stack = []

n = len(part)

for char in s:
    # see if past n in stack == part then remove
    stack.append(char)
    if len(stack) >= n:
        tmp = ''.join(stack[-n:])
        if tmp == part:
            del stack[-n:]

answer = ''.join(stack)
return answer