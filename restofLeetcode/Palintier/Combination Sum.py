#here we are given an array and a target integer. We need to find all possible solutions within that array that can add up to that integer

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