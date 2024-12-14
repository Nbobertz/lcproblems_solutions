#here we are going to be given an array of integers and the goal is to find all possible combinations that add up to a target. This problem involves backtracking over a weird decision tree as we have to isolte each integer into it's own branch

candidates = [2,3,6,7]
target = 7

def solution():
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res

print(solution())