"""
Here we are just seeing what the max depth is
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # this is a dfs, classic one

        answer = 0
        if not root:
            return answer

        def dfs(root, tmp):
            nonlocal answer

            if not root:
                answer = max(answer, tmp)
                return

            dfs(root.left, tmp=tmp + 1)
            dfs(root.right, tmp=tmp + 1)
            return

        dfs(root, 0)
        return answer