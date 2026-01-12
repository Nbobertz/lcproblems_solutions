"""
This is path sum nodes
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        #this is a dfs problem
        if not root:
            return []

        answer = []

        def dfs(root,ss,path):
            nonlocal answer
            #ss =sum so far, path == nodes so far
            if not root:
                return

            path.append(root.val)
            ss+=root.val

            if not root.left and not root.right and ss == targetSum:
                answer.append(path.copy())

            dfs(root.left,ss,path)
            dfs(root.right,ss,path)

            path.pop()
            return

        dfs(root,0,[])
        return answer