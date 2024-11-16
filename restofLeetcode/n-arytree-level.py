#here we are going to be given an n-aray with the sublist called children. Our goal is to print off each child into a subarray based off their level in the tree.

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = collections.deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            result.append(level)
        return result



#the idea here is that we bfs into the tree and then begin the process of bfs through the tree to capture each individual level and add the child to that level. I got held up on this problem becasue of the child function being an array in of itself.