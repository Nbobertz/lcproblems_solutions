#here we are going to be given an array with integers. The idea is that you have to find all subsets in that array. This is a dfs problem

nums = [1,2,3]

def solution():
    # first create the result array
    res = []

    # then we create the subset array, this adds all subsets to array
    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        # decision to include
        subset.append(nums[i])
        dfs(i + 1)

        # decision to not include
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res

print(solution())