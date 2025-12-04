"""
Just do the normal option and then inverse the inorder list so that it is inverse. Pretty simple if you use the [::-1]


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

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

                sub.append(node.val)

                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)

            answer.append(sub)

        return answer[::-1]