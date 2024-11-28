#here we are going to be given a bst and we have to find the kth smallest element in the tree. I solved this on my own with a bst and simply sorting hte array at the end and returning the element.

# def solution():
#     # bfs add to a stack
#     q = deque()
#
#     if not root:
#         return 0
#
#     q.append(root)
#     arr = []
#     while q:
#         for x in range(len(q)):
#             node = q.popleft()
#             arr.append(node.val)
#             if node.left != None:
#                 q.append(node.left)
#             if node.right != None:
#                 q.append(node.right)
#     arr.sort()
#     return arr[k - 1]