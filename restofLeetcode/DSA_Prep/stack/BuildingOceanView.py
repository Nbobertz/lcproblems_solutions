"""
This is just a stack problem to see the max number of ocean view buildings


"""


class Solution(object):
    def findBuildings(self, heights):
        # this is a stack problem
        stack = []
        answer = []

        # edge case of not heights
        if not heights:
            return answer

        # I keep count and sub to get to end of array, sure there is another way
        count = 0
        for b in heights[::-1]:
            if count == 0:
                stack.append(b)
                answer.append(((len(heights) - count) - 1))
                count += 1
            else:
                # check top of stack
                if b > stack[-1]:
                    stack.append(b)
                    answer.append(((len(heights) - count) - 1))
                    count += 1
                elif b <= stack[-1]:
                    count += 1
        answer.sort()
        return answer

