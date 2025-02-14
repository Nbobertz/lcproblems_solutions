#here we are consting a quad tree. This is the basis for postgis and allows a map to be divided into 4ths.

def solution(self, grid: List[List[int]]) -> 'Node':
    # the idea here is that we need to dfs
    def dfs(n, r, c):
        same = True
        for i in range(n):
            for j in range(n):
                if grid[r][c] != grid[r + i][c + j]:
                    same = False
                    break

        # base case
        if same:
            return Node(grid[r][c], True)

        n = n // 2  # int division
        topleft = dfs(n, r, c)
        topright = dfs(n, r, c + n)
        bottomleft = dfs(n, r + n, c)
        bottomright = dfs(n, r + n, c + n)

        return Node(0, False, topleft, topright, bottomleft, bottomright)

    return dfs(len(grid), 0, 0)