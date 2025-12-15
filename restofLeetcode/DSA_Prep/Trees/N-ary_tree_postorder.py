"""
Append from the bottom up

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # just dfs to the bottom and append on teh way to the top
        answer = []
        if not root:
            return answer

        def dfs(root):
            nonlocal answer
            if not root:
                return

            child = root.children
            for c in child:
                dfs(c)

            answer.append(root.val)
            return

        dfs(root)
        return answer