#Here we are given a series of daily temperatures and must return an array where each index is the max amount of days it would take to see a higher temperature.

#here is a o(n2) solution that involves two loops.

temperatures=[89,62,70,58,47,47,46,76,100,70]
class Solution:
    def dailyTemperatures(temperatures):
        # we can do two pointer here

        answer = []

        for p1 in range(0, len(temperatures)):
            count = 1
            r = p1 + 1
            while r < len(temperatures):
                if temperatures[p1] < temperatures[r]:
                    answer.append(count)
                    break
                elif temperatures[p1] >= temperatures[r]:
                    r += 1
                    count += 1

                if r == len(temperatures):
                    count = 0
                    answer.append(count)
                    break
            if p1 == len(temperatures) - 1:
                answer.append(0)
                return answer

        return answer

answer1 = Solution.dailyTemperatures(temperatures= temperatures)
print(answer1)

class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures) #create a bunch of 0 points to fill result array
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i-stackInd)
            stack.append([t,i])
        return res