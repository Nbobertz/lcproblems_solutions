"""
The idea here is that we have leaf similar trees taht we need to solve
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # we can do this with a bfs and just capture the leaf nodes

        if not root1 or not root2:
            return False

        # compare these two
        n1, n2 = [], []

        def dfs(root, arr):
            if not root:
                return

            if root.left == None and root.right == None:
                arr.append(root.val)
                return

            if root.left:
                dfs(root.left, arr)
            if root.right:
                dfs(root.right, arr)

            return

        dfs(root1, n1)
        dfs(root2, n2)
        if n1 == n2:
            return True
        else:
            return False