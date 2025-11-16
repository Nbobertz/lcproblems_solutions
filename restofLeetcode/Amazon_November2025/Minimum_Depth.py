"""
This is just what is the minimum depth with a solo node in a tree

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        import math
        q = deque()

        # so for this problem I think what's best is to bfs down until we find a leaf node, keep track of shortest
        short = None

        if not root:
            return 0

        q.append(root)

        while q:
            # we are on next level down
            if short == None:
                short = 1
            elif short != None:
                short += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left == None and node.right == None:
                    return short

                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)