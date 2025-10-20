"""here we loop through the input string one time to determine if it is a valid paranthesis"""

s = '[][][][][][][][][][][][]()()()()()()()'
def isValid(s):
    stack = []
    closeToOpen = {")": "(", "]": "[", "}": "{"}

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False

print(isValid(s=s))