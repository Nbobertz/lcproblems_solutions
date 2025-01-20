#here we will be doing a classic problem. Flood fill. We start at a point in a matrix and have to change all colors of it based off integer values.
#this is a classic recursion dfs problem.

image = [[1,1,1],
         [1,1,0],

         [1,0,1]]
sr = 1
sc = 1
color = 2

def solution():
    # here we are given a graph and the idea is that we will have to look at all other pixels around it and determine if it will flood if we dropped water on it.

    # capture number of rows
    m = len(image)  # number of rows
    n = len(image[0])  # number of columns
    orgColor = image[sr][sc]

    # if target color is same as origional; no changes are needed
    if orgColor == color:
        return image

    # build dfs function and call it
    def dfs(row, col):
        # base case; out of bounds.
        if (row < 0 or row >= m
                or col < 0 or col >= n
                or image[row][col] != orgColor):
            return

        # update pixel color
        image[row][col] = color

        # recursivly visit all neighbors until out of bounds
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

        # this above block is responsible for us going in all four directions and checking the logic

    dfs(sr, sc)  # start at designated starting point
    return image

print(solution())