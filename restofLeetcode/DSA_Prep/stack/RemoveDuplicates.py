"""
The idea is that you have to iterate through and remove k characters that are the same. You are given the array and k integer to remove
"""


class Solution(object):
    def removeDuplicates(self, s, k):
        # the idea here is that we can use a stack and append from the [-3] and see if it's duplicate. IF it is then we pop and continue

        answer = ''
        if not s or not k:
            return answer

        stack = []

        for char in s:
            if len(stack) >= 3:
                top = stack[-1]
                tmp = [top] * k
                if stack[-k:] == tmp:
                    del stack[-k:]
            stack.append(char)

        # check last 4
        top = stack[-1]
        tmp = [top] * k
        if stack[-k:] == tmp:
            del stack[-k:]
        answer = ''.join(stack)
        return answer
