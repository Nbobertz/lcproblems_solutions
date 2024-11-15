#here we are given a binary tree and we have to find the lowest common ancestor. Since there is not rhyme on how the tree is set up we will have to iterate through at max every node to find the lowest common ancestor. Due to this we can call DFS recursivly to go down each subtree arm until we find the node and then return that path. After this we then return the root as it is the answer.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        return l or r

#do on leetcode as they have the test cases.