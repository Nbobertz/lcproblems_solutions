"""
THis is just the maximum depth problem of a tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # this is a dfs problem where we simply keep a max number and return that as we go down
        answer = 0
        if not root:
            return answer

        answer = 1

        def dfs(root, tmp):
            nonlocal answer

            # base case
            if not root:
                return 0

            tmp += 1

            ll, rr = dfs(root.left, tmp), dfs(root.right, tmp)
            answer = max(answer, max(ll, rr))
            return tmp

        dfs(root, 0)
        return answer