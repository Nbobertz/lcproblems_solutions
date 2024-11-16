#did this one by myself in record time. It is just a simple bfs

#here we are given a level binary tree. We have to iterate through it and return the tree's structure via nested arrays.

# # deque allows pop from left. Allows us to add and take away in one motion
# q = deque()
# if root == None:
#     return []
#
# q.append(root)
#
# # create the answer array
# answer = []
#
# # for BFS we call the len of q, put a for loop inside to constantly open each 'node' and pop it's subnodes to list
# while len(q) != 0:
#     answer.append([])
#     for p1 in range(0, len(q)):
#         node = q.popleft()
#         answer[-1].append(node.val)
#         if node.left != None:
#             q.append(node.left)
#         if node.right != None:
#             q.append(node.right)
#
# return answer


#the trick here is to simply use a bfs and capture each 'round' into the subarray that is constructed inbetween each round.