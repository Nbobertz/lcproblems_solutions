"""
This is to find a path sum to a leaf node
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # this is a dfs problem. We simply check all possible paths and return True if we found an integer
        answer = False

        if not root:
            return answer

        def dfs(root, ss):
            nonlocal targetSum, answer
            if not root:
                return

            ss += root.val
            if root.left == None and root.right == None and ss == targetSum:
                answer = True
                return

            dfs(root.left, ss)
            dfs(root.right, ss)
            return

        dfs(root, 0)
        return answer