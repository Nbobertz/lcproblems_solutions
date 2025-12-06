"""
This is a sum traversal recursion tree algorithm
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sumLeft(head, isLeft=False):
            if head is None:
                return 0

            if head.left is None and head.right is None:
                return head.val if isLeft else 0

            return sumLeft(head.left,True) + sumLeft(head.right)

        return sumLeft(root)