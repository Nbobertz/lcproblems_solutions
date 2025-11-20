"""
This is just the daily temps problem. It's the classic monotomic stack and I finally am starting to get the hange of it
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # this is a monotomic stack problem; the monotomic stack problem.
        # this is because the stack will always be decreasing. The trick here is to append the number and index then capture the delta

        # first check edge constraints
        if not temperatures:
            return []

        # I mispell stuff all the time, this helps
        temps = temperatures

        # now build answer array defaulting all possible date's to 0's to store
        answer = []
        for _ in range(len(temps)):
            answer.append(0)

        # now we are going to init the stack
        stack = []  # here we are going to store (n,i) where n = number at the i = index

        for i, n in enumerate(temps):
            if not stack:
                stack.append((n, i))
            else:
                # handle easy case first, what if n <= stack[-1][0]; not greater continue
                if n <= stack[-1][0]:
                    # add to sack, its less or equal
                    stack.append((n, i))

                # now what if the number is greater?
                elif n > stack[-1][0]:
                    # we will continue down the stack until it's no longer greater
                    while stack and n > stack[-1][0]:
                        n2, i2 = stack.pop()
                        answer[i2] = i - i2  # remember that answer array of 0's, now we replace the 0 with the delta
                    # make sure to append your current to the stack
                    stack.append((n, i))
        return answer

