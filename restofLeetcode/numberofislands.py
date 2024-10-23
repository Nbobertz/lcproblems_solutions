#Here we are going to be given a set of 2d binary arrays comprised of 1's and 0's. The idea here is that if you have enough 1's you have an island. 0's are water. only 1's connected adjacently or vertically can be considered an island.

#I think the easiest solution here is going to be a hashmap. The idea is that we will loop over each array and see if we have a 1. If we do then we check to see if any other 1's connect either vertically or horizontally. If they do we count that as an island.

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]

def solution():
    width = len(grid[0])
    height = len(grid)
    hashm = {}

    for p1 in range(0,height):
        strip=grid[p1]
        for p2 in range(0,width):
            if strip[p2] == '1':
                if p2!=0:
                    hashm.update({p1:p2})

#so the trick here is to use depthbreathsearch. THis is from leetcode premium. Need to study up on how to impliment this.
def solution2():
    from collections import deque
    islands =0
    rows, cols = len(grid), len(grid[0])

    def bfs(r,c):
        q = deque()
        q.append((r,c))
        grid[r][c]=0

        while q:
            row,col = q.popleft()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for dr, dc in directions:
                r,c = row +dr, col +dc
                if 0<= r< rows and 0 <= c <cols and grid[r][c] == '1':
                    q.append((r,c))
                    grid[r][c] = '0'

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands+=1
                bfs(r,c)

    return islands

a = solution2()
print(a)