"""
This is the classic DFS problem where we are instructed to open the lock
"""

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ss = set(deadends)

        if '0000' in ss:
            return -1

        def dfs(cur):
            #check all possible current combiantions by 1 and -1
            res = []
            for x in range(4):
                tmp = str((int(cur[x])+1)%10)
                res.append(cur[:x]+tmp+cur[x+1:])

                tmp = str((int(cur[x])-1+10)%10)
                res.append(cur[:x]+tmp+cur[x+1:])
            return res

        from collections import deque
        q = deque()

        q.append(['0000',0]) #current lock and count
        while q:
            for _ in range(len(q)):
                lock,count = q.popleft()

                if lock == target:
                    return count

                for poss in dfs(lock):
                    if poss not in ss:
                        ss.add(poss)
                        q.append([poss,count+1])
        return -1