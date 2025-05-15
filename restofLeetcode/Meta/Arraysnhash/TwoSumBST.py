#this is a bst problem. Descend through the nodes and figure out if the node.val + node.val == target (k)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        #this is a bfs problem, we stop as soon as we hit two numbers that hit

        q = deque()

        if root == None:
            return False

        #root exists add to q
        q.append(root)

        #array to store
        arr = []

        #pop
        while q:
            node = q.popleft()
            tt = k - node.val
            if tt in arr:
                return True
            arr.append(node.val)

            #if node left or right append
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)

        return False