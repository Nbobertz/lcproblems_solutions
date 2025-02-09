#Here we are given an array of integers and we need to return ALL subsets of that array as subarrays.
#the idea here is that we have to use backtracking to get everything in the array. This is because with backtracking we can hit and pop everything on the left most point of a tree as we make decisions.

#Hint: If a problem requires ALL sub of an input be returned it more then likely will be backtracking

#below is test case
nums = [1,2,3]

def solution():
    # so we first need to create a temporary working subarray and a result array

    res, sub = [], []

    def dfs(i):

        #first is capture base case
        if i >= len(nums):
            res.append(sub.copy())
            return

        #decision to include nums[i] and continue down tree
        sub.append(nums[i])
        dfs(i+1)

        #decision to not include
        sub.pop()
        dfs(i+1)

    dfs(0)
    return res

print(solution())