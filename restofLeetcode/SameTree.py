#here we are going to be given two tree's p and q. The idea is that you need to be able to tell me if the two trees are the same or not. If they are you simply return True or False

#this is a good prolem to practice recursion on.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
# #         self.left = left
# #         self.right = right
#
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         # first we capture edge case of both tree's being null, then we compare the node at both trees. If it ends then we simply return False
#         if not p and not q:
#             return True
#         if not p or not q or p.val != q.val:
#             return False
#
#         return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))