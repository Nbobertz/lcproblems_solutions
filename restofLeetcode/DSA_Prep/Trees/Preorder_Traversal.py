"""
This is the preorder traversal problem. Simply iterate throug the tree
"""

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        if not root:
            return answer


        #recursion loop, grab left and add, grab right and add, return on null rot
        def dfs(root,answer):
            if not root:
                return

            answer.append(root.val)
            if root.left:
                dfs(root.left,answer)
            if root.right:
                dfs(root.right,answer)
            return answer

        answer = dfs(root,answer)
        return answer