#here we are going to be given two strings. The goal is to find out if it is possible to switch only two characters to make both strings the same.

s = "ab"
goal = "ba"

def solution():
    if len(s)!=len(goal):
        return False
    if s==goal and len(set(s))<len(s):
        return True
    diff = []
    for x in range(0,len(goal)):
        if s[x] !=goal[x]:
            diff.append((s[x],goal[x]))
    if len(diff)==2 and diff[0]==diff[-1][::-1]:
        return True
    return False

answer = solution()
print(answer)