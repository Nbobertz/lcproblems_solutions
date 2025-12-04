"""
This is just bfs and keeping track of what characters you see at what points
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #this is just a bfs problem

        answer = []

        if not root:
            return answer


        from collections import deque
        q = deque()
        q.append(root)

        while q:
            sub = []
            for _ in range(len(q)):
                node = q.popleft()

                #append to sub
                sub.append(node.val)

                #check left and right
                if node.left != None:
                    q.append(node.left)

                if node.right != None:
                    q.append(node.right)

            answer.append(sub)

        return answer