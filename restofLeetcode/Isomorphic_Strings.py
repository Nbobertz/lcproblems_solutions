#Here we are given two strings and have to determine if they are isomorphic.

#exmaple
s = "foo"
t = "baa"

def solution():
    # if len does not match return False
    if len(s) != len(t):
        return False

    # create a hashmap
    stack1 = []
    stack2 = []

    # loop through words and check
    for p1 in range(len(s)):
        print(s[p1],t[p1])
        print(stack1,stack2)
        if len(stack1) == 0:
            stack1.append(s[p1])
            stack2.append(t[p1])
        elif s[p1] == stack1[-1] and t[p1] != stack2[-1]:
            return False
        elif t[p1] == stack2[-1] and s[p1] != stack1[-1]:
            return False
        stack1.append(s[p1])
        stack2.append(t[p1])
    return True

print(solution())