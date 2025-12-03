"""
Here is me doing a balanced binary tree via recursion problem
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #we can do this with a recursive dfs

        if not root:
            return True

        def dfs(root):
            if not root:
                #we are at base case of nothing or no node
                return [True,0]

            left,right = dfs(root.left),dfs(root.right)

            balanced = (left[0] and right[0] and
                        abs(left[1]-right[1])<=1)

            return [balanced, 1 + max(left[1],right[1])]

        answer = dfs(root)

        if answer[0] == True:
            return True
        else:
            return False