#imports
import time


#the goal here is that we have an integer array called nums. The idea here is to return all subsets of the array.
#a subset is simply sub array. So for 1,2,3 it would be [],[1],[2],[3],[1,2], etc.

nums = [1,2,3]

def solution():
    #first create a result array that we will append stuff to
    res = []

    #now we create the subset array
    subset = []

    #create recursive dfs
    def dfs(i):
        print(i)
        if i>=len(nums):
            #here we are going to say that if the ith position is greater then len(nums) then we will stop and append subset to the result array
            res.append(subset.copy())
            print('append',subset)
            time.sleep(1)
            return

        #decision to include
        subset.append(nums[i])
        # print('include',nums[i])
        # print(subset)
        print(subset)
        time.sleep(1)
        dfs(i+1)

        #decision to not include
        num=subset.pop()
        print('pop',num)
        print(subset)
        time.sleep(1)
        dfs(i+1)
    dfs(0)
    return res



def solution2():
    n = len(nums)
    res,sol = [],[]

    def backtrack(i):

        #capture base case; at end of nums array
        if i == n:
            res.append(sol[:])
            print('return',res, i)
            time.sleep(1)
            return

        #pick nums[i]
        sol.append(nums[i])
        print(sol,i)
        time.sleep(1)
        backtrack(i+1)
        sol.pop()

        # don't pick nums[i]
        backtrack(i + 1)

    backtrack(0)
    return res
print(solution2())