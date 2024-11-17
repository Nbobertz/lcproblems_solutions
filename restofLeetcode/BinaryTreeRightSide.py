#here we are given a binary tree and the idea is that you want to return the node.val's that are viewalble from the right side only. This is a BFS problem with the caviaet that you will pull from the right hand side each time.

#test this on LC since we don't have the tree const.

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # We can do this with bfs. Just append to answer arry .right. Trick is to know bfs.
        q = deque()

        # capture null
        if root == None:
            return []

        # const array
        answer = []
        # answer.append(root.val)

        # add root
        q.append(root)

        # bfs
        while len(q) != 0:
            layer = []
            for p1 in range(0, len(q)):
                node = q.popleft()
                layer.append(node.val)
                # node.right exists and append
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            answer.append(layer[-1])
        return answer