"""
Here we are given a binary tree and have to determine it's max depth. The idea is that we keep track of each of the levels

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        depth = 0
        if not root:
            return 0

        q = collections.deque()
        node1 = root
        q.append(node1)
        while q:
            level = len(q)
            for _ in range(level):
                node = q.popleft()
                if node.left!=None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            depth+=1

        return depth