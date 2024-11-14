#redid the max depth problem. Got better at bfs

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         #here we are going to be given a tree and we want to see it's maximum depth. The goal here is to use bfs to catch all avaliable nodes in the 'depth' and then iterate to a counter. At the end we return the counter.
#
#         #first we construct the q
#         q = deque()
#         #now we catch base case
#         if root==None:
#             return 0 #this is to return the 0 as there is not root
#
#         #append root to q since it exists
#         q.append(root)
#
#         #counter for depth
#         counter=0
#         #now we bfs
#         while len(q)!=0:
#             for p1 in range(0,len(q)):
#                 node = q.popleft()
#                 if node.left!=None:
#                     q.append(node.left)
#                 if node.right!=None:
#                     q.append(node.right)
#             counter+=1
#         return counter

#here we built a bfs solution to scan for the maximum depth in a tree. THe idea is that in your tree you will add to a q and then iterate in a while and for loop to get all things inside of the level. We then add another iteration and increase counter until the len of q is 0