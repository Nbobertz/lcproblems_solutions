#here we are given a tree and we have to iterate through it and add the value of each node to the array. This one I did by myself and it invovled a bfs algorithm

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # this is a bfs problem. We will iterate through the tree and return the node.val into an array
        # use a deque to popleft
        q = deque()

        # catch base case of None root
        if root == None:
            return []

        # now we append root to q. This is to 'prime' the bfs
        q.append(root)

        # Create answer array
        answer = []

        # now bfs
        while len(q) != 0:
            answer.append([])
            for p1 in range(0, len(q)):
                node = q.popleft()
                # append node.val to answer. Only works because it is left to right
                answer[-1].append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)

        return answer