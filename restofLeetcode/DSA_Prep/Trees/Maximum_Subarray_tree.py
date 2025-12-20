"""
This is for gettign the maximum subarray value of a tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.answer = 0.0

        def dfs(node):
            if not node:
                return (0, 0)  # (sum, count)

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            self.answer = max(self.answer, total_sum / total_count)

            return (total_sum, total_count)

        dfs(root)
        return self.answer