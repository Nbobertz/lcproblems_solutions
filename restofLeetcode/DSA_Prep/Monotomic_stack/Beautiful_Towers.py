"""
This is a monotonic stack. The idea here is that we have to create mountains. This is used with a monotonic stack
"""
def solution():
    n = len(heights)

    left = [0] * n
    right = [0] * n

    # compute left
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] > heights[i]:
            stack.pop()

        if stack:
            j = stack[-1]
            left[i] = left[j] + (i - j) * heights[i]
        else:
            left[i] = (i + 1) * heights[i]

        stack.append(i)

    # compute right
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] > heights[i]:
            stack.pop()

        if stack:
            j = stack[-1]
            right[i] = right[j] + (j - i) * heights[i]
        else:
            right[i] = (n - i) * heights[i]

        stack.append(i)

    # compute best peak
    ans = 0
    for i in range(n):
        ans = max(ans, left[i] + right[i] - heights[i])

    return ans