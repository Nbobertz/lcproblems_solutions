"""
Got this one first try


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return roo1

        def dfs(root, arr):
            if not root:
                return

            if root.left == None and root.right == None:
                arr.append(root.val)
                return arr

            dfs(root.left, arr)
            dfs(root.right, arr)
            return arr

        arr1 = dfs(root1, [])
        arr2 = dfs(root2, [])
        print(arr1, arr2)
        return arr1 == arr2