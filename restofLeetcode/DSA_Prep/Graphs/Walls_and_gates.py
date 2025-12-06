"""
here is a bfs solution for walls and gates
"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        from collections import deque
        if not rooms:
            return

        ROWS, COLS = len(rooms), len(rooms[0])
        INF = 2147483647
        q = deque()

        # 1. Start BFS from all gates
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # 2. BFS
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Only update INF cells
                if 0 <= nr < ROWS and 0 <= nc < COLS and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))