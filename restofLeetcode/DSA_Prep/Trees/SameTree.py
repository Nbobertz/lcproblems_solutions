"""
Here they have the same tree problem
"""

# if not p and q or p and not q:
#     return False

from collections import deque


def check(p, q):
    q1 = deque()
    q2 = deque()

    q1.append(p)
    q2.append(q)

    while q1 and q2:
        for _ in range(len(q1)):
            node1 = q1.popleft()
            node2 = q2.popleft()

            # check vals
            if node1 is None and node2 is None:
                continue

            if node1 is None or node2 is None or node1.val != node2.val:
                return False

            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.left)
            q2.append(node2.right)
    return True


answer = check(p, q)
return answer