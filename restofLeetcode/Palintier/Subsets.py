#given an array find all possible subsets. This is backtracking at it's finest

nums = [1,2,3]

def solution():
    # create a length variable so that we don't go out of bounds
    n = len(nums)

    # initalize two array's for result(res) and solved(sol)
    res, sol = [], []

    # define backtrack function
    def backtrack(i):
        # handle the base case of if i is at the len of n
        if i == n:
            res.append(sol[:])
            return

        # dont pick nums[i]
        backtrack(i + 1)

        # pick nums of i. This will push the nums of i into solved, then backtrack against that solved variable, then pop the ith index
        sol.append(nums[i])
        backtrack(i + 1)
        sol.pop()

    backtrack(0)
    return res