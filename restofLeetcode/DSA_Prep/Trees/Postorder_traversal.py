"""
This is a binary tree postorder traversal problem. The idea here is that we are going to go down until child and then add
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        if not root:
            return answer


        def dfs(root):
            nonlocal answer

            if not root:
                return

            dfs(root.left)
            dfs(root.right)
            answer.append(root.val)
            return

        dfs(root)
        return answer