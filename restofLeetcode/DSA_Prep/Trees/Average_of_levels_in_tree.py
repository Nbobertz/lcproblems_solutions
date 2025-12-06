"""
This is the average of the levels in the tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        answer = []
        if not root:
            return answer

        from collections import deque
        q = deque()
        q.append(root)

        while q:
            count = 0
            running = 0
            for _ in range(len(q)):
                node = q.popleft()

                # calc ave
                running += node.val
                count += 1

                if node.left != None:
                    q.append(node.left)

                if node.right != None:
                    q.append(node.right)

            ave = (running / count)
            answer.append(ave)

        return answer



