#here we are given a binary tree and we want to return the maximum depth of the tree (amoutn of leafs down)
#have to submit on leetcode as they have answers

# def solution():
# q = deque()
# if root != None:
#     q.append(root)
# 
# # now we bfs across the layers. If the node.left or node.rigt exists we append the .left or .right to the deque and continue. We have a counter to keep track of maximum depth. We go until q is empty
# counter = 0
# while q:
#     for x in range(0, len(q)):
#         node = q.popleft()
#         if node.left != None:
#             q.append(node.left)
#         if node.right != None:
#             q.append(node.right)
#     counter += 1
# return counter