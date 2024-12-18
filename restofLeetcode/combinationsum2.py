#here we are given an array of integgers called nums and it is our job to figure out how many diffrent combinations you can have to reach a target integer.

#you can use the same number multiple times but you can only have one unique combination per round.

nums =[2,5,6,9]
target = 9

def solution():
    #create a result array
    res = []

    #recursive depth for search
    def dfs(i,cur,total):
        if total==target:
            res.append(cur.copy())
            return
        if i>len(nums) or total > target:
            return

        cur.append(nums[i])
        dfs(i,cur,total+nums[i])
        cur.pop()
        print(res)
        dfs(i+1,cur,total)

    dfs(0,[],0)
    return res

print(solution())