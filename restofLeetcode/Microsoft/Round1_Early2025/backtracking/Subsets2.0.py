#here we are given an array of integers and we need to figure out all subsets of those integers. A subset is an integer combo made up of the input integers.
#this is a dfs recursion problem. You dfs down through the decision tree until you get to a point where you can return.

nums = [1,2,3]

def solution():
    #this is a recursion problem. The idea here is that we need to iterate down through a decision tree and append to a subarray.

    #const your arrays. We wll have two; one to work from and one to copy result.
    answer = []
    sub = []

    #build your dfs function
    def dfs(i):

        #capture base case; hit end of nodes on decision return
        if i >= len(nums):
            answer.append(sub.copy())
            return

        #append to sub array
        sub.append(nums[i])

        #dfs call
        dfs(i+1)
        #pop from subarray to move back
        sub.pop()

        #go from next number
        dfs(i+1)


    #capture base case of no nums
    if nums:
        dfs(0)
    else:
        return []

    return answer

print(solution())