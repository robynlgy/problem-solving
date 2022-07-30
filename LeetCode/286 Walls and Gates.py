# You are given an m x n grid rooms initialized with these three possible values.

# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        #bfs bcz we are finding shortest distance
        #rather than bfs at each cell, bfs from gate
        #dont have to do anything about inf bcz they were alr inf

        ROWS, COLS = len(rooms), len(rooms[0])
        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        steps = 1

        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    queue.append((i,j))


        while queue:
            for i in range(len(queue)):
                (r,c) = queue.popleft()

                for dr, dc in DIRECTIONS:
                    row, col = r+dr, c+dc
                    if (row < 0 or row >= ROWS or
                       col < 0 or col >= COLS or
                       rooms[row][col] != 2147483647):
                        continue
                    queue.append((row,col))
                    rooms[row][col] = steps
            steps += 1



