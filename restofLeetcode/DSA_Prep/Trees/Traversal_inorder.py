"""
The idea here is that you will have to do a dfs inorder traversal to get through all nodes in the tree
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        #this is a dfs problem. We simply need to iterate through everything and return

        answer = []

        if not root:
            return answer

        def dfs(root):
            nonlocal answer
            if not root:
                return


            answer.append(root.val)
            child = root.children
            for c in child:
                dfs(c)
            return


        dfs(root)

        return answer