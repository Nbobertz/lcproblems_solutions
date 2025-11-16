"""
Iterate down through the tree and return the BFS value
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # so we just bfs down and keep track of what we see

        if not root:
            return 0

        q = deque()

        q.append(root)

        seen = set()

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                seen.add(node.val)

                # add nodes
                if node.left != None:
                    q.append(node.left)

                if node.right != None:
                    q.append(node.right)

        # now we are going iterate through set and return min
        seen = list(seen)
        if len(seen) == 1:
            return 0
        seen.sort()
        answer = max(seen)

        print(seen)

        l, r = 0, 1
        while r != len(seen):
            tmp = abs(seen[r] - seen[l])
            answer = min(answer, tmp)
            l += 1
            r += 1
        return answer