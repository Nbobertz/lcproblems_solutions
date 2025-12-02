"""
Here we are looking for a diamater of binary tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0

        if not root:
            return answer

        def dfs(root):
            nonlocal answer

            #handle base case
            if not root:
                return 0 #we return 0 because there is no other edges

            left = dfs(root.left)
            right = dfs(root.right)
            answer = max(answer,right+left) #updates the largest tree diamater we see
            return 1 + max(right,left)

        dfs(root)
        return answer