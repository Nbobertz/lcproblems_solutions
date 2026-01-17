"""
This is the classic monotonic stack problem. The trick is to use a tuple while popping
"""

if not temperatures:
    return []

answer = [0] * len(temperatures)

stack = []  # monotonic, streactly decreasing

for i, n in enumerate(temperatures):
    if not stack:
        stack.append((n, i))
    elif n <= stack[-1][0]:
        stack.append((n, i))
    elif n > stack[-1][0]:
        while stack and n > stack[-1][0]:
            answer[stack[-1][1]] = i - stack[-1][1]
            stack.pop()
        stack.append((n, i))
return answer