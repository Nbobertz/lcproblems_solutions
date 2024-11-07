#here we are given a tree and have to figure out the largest path between the nodes. The idea is that you do breath for search,bfs, to figure out the largets diameter on the tree and store that variable as the max. Below is the solution for recursive call.

# def solution():
#     self.res = 0
#
#     # return the height
#     def dfs(curr):
#         if not curr:
#             return 0
#
#         left = dfs(curr.left)
#         right = dfs(curr.right)
#
#         self.res = max(self.res, left + right)
#         return 1 + max(left, right)
#
#     dfs(root)
#     return self.res