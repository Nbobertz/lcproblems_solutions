#here we are given an integer array nums we need to retturn all possible subsets of the array
nums = [1,2,3]

class Solution:
    def __init__(self):
        self.answer = []
        self.tmp = []

    def solution(self):
        #this is a backtracking solution. We need to iterate through the entire decision tree and add it to the answer array



        def dfs(i):

            #capture base case
            if i >= len(nums):
                self.answer.append(self.tmp.copy())
                return

            #append tmp
            self.tmp.append(nums[i])

            #bfs down
            dfs(i+1)
            #pop off tmp
            self.tmp.pop()
            dfs(i+1)


        if nums:
            dfs(0)
        else:
            return "No input, no solution possible"

        return self.answer

s = Solution()
answer = s.solution()
print(answer)