#here we are going to be given a binary tree and we have to count the good nodes in that tree. Here the idea is that a node is considered good if we can go all the way back to root in the same path without having a larger number (0,1,2,3,4,5).

#this algorithm is a DFS since it goes all the way down before going sideways.

#test in LC due to not having proper tree tests

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Here we build an iterative subfunction called DFS
        def dfs(node, maxVal):
            # captures base case of no root, returns 0 for nothing there
            if not node:
                return 0

            # now we are going to build out the logic meaning we found a node
            if node.val >= maxVal:
                res = 1
            else:
                res = 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)