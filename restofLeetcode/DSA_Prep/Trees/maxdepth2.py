"""
Second time doing this problem
"""

if not root:
            return 0

        from collections import deque
        q = deque()
        q.append(root)

        depth = 0

        while q:
            depth+=1
            for _ in range(len(q)):
                node = q.popleft()

                if node.left != None:
                    q.append(node.left)

                if node.right != None:
                    q.append(node.right)
        return depth