#The idea here is that you have a bst and that it has numbers as sum. You have to iterate through the tree and if you get to the target with the sum you return True, else it is false.
#run on LC as they have the tree's

def solution():
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
            # this is a bfs problem, we stop as soon as we hit two numbers that hi the integer k

            # get the base case
            if root == None:
                return False

            # if binary tree is only 1 level

            answer = False

            # create the deque
            q = deque()

            # at this point we know the root exists and have deque
            q.append(root)

            # create array
            arrlen = []

            while len(q) != 0:
                for x in range(0, len(q)):
                    node = q.popleft()
                    arrlen.append(node.val)

                    if node.left != None:
                        q.append(node.left)

                    if node.right != None:
                        q.append(node.right)

            if len(arrlen) == 1:
                return False

            for p1 in range(0, len(arrlen)):
                for p2 in range(p1 + 1, len(arrlen)):
                    if arrlen[p1] == None or arrlen[p2] == None:
                        continue
                    elif arrlen[p1] + arrlen[p2] == k:
                        answer = True
            return answer

