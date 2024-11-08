#here we are going to be given a tree and the idea is that we will have to iterate through it to figure out if hte tree is balanced or not.

# def solution():
#     # turns out you want to run dfs to get the maxumum depth of each node. From here you make sure the tree is balenced
#
#     # we build out a function to do this recursivly
#     def dfs(root):
#         if not root:
#             return [True, 0]
#
#         left, right = dfs(root.left), dfs(root.right)
#         balanced = (left[0] == True and right[0] == True and
#                     abs(left[1] - right[1]) <= 1)
#
#         return [balanced, 1 + max(left[1], right[1])]
#
#     return dfs(root)[0]