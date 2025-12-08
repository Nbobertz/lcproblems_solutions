"""
This is a dfs binary tree problem. Did it optimally with o(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        #This is a dfs problem

        if not root:
            return root


        answer = []
        path = []
        def dfs(root):
            if not root:
                return
            path.append(str(root.val)) #have a list of strings of integers
            if not root.left and not root.right:
                answer.append('->'.join(path))
            else:
                dfs(root.left)
                dfs(root.right)
            path.pop()

        dfs(root)
        return answer