"""
Here you need to find a subtree of another tree
"""

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True
        if not root:
            return False

        def compare(r, s):
            if not r and not s:
                return True
            if not r or not s:
                return False
            if r.val != s.val:
                return False
            return compare(r.left, s.left) and compare(r.right, s.right)

        # Check if they match here OR search left subtree OR right subtree
        return (
            compare(root, subRoot) or
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )