#here we are going to be given a tree and the idea is that we need to be able to return the max value at each layer in the tree
#do this on LC as I don't have test cases.

def solution():
    # this is a bfs search down a tree. we simply scan the q after each 'row' and append the largest to an answer array
    answer = []

    # data structure is a deque. Assuming collections. is imported
    q = deque()

    # capture no root
    if not root:
        return []  # could change if we have nothing
    else:
        q.append(root)

    # now we while loop on the q, after each iteration we simply take the largest and scan. The end result is an array of len == 'layers' of the tree

    while q:
        length = len(q)
        cur_max = float('-inf')

        for _ in range(length):
            node = q.popleft()
            cur_max = max(cur_max, node.val)
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)

        answer.append(cur_max)
    return answer

