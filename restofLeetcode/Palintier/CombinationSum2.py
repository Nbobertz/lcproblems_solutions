#here we are given an arraay and a target. We have to return all possible combinations that add up to the target and we can only use each number once.

candidates = [10,1,2,7,6,1,5]
target = 8

def solution():
    res = []
    candidates.sort()

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if total > target or i == len(candidates):
            return

        cur.append(candidates[i])
        dfs(i + 1, cur, total + candidates[i])
        cur.pop()

        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res

print(solution())