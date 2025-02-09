#here we are given an array integers and a target integer. You need to return all possible solutions that will sum up to the target integer.

#we can return multiple of the same integer but only one version of that.

#this is a backtracking problem. The idea here is that you loop through all decisions and see if it sums up to the value.

nums = [2,5,6,9]
target = 9

def solution():

    #here we are going to create two subarrays. Res, and sub. The idea here is that we are going to use sub as a temporary working array and only append if we don't see it in the res array.

    res=[]

    def dfs(i,cur,total):


        #handle base case
        if total==target:
            res.append(cur.copy())
            return
        if i >= len(nums) or total > target:
            return

        #decision to include
        cur.append(nums[i])
        dfs(i,cur,total+nums[i])
        cur.pop()
        dfs(i+1,cur,total)

    dfs(0,[],0)
    return res

print(solution())