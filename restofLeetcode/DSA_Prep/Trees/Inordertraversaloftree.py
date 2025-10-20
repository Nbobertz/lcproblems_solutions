#https://leetcode.com/problems/binary-tree-inorder-traversal/


def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # recursive call to bottom, find bottom and append to res array value, go up and do it again.-DSA_Prep

    res = []

    def inorder(root):
        if not root:
            return  # base case caught

        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)
    return res
