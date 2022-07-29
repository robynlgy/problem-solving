# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # instead of bfs from fresh oranges, find the rotten ones and bfs from them, changing fresh -> rotten --> this mutates the input
        # if there are more than 1 rotten, add both to the initial queue "multi-source bfs"
        # to check if its possible to rot it all, we can initialize the # of total fresh oranges, at the end this number should be 0

        ROWS, COLS = len(grid), len(grid[0])
        fresh, time = 0, 0
        queue = deque()
        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i,j))

        while queue and fresh > 0:

            for i in range(len(queue)):
                r,c = queue.popleft()

                for dr, dc in DIRECTIONS:
                    row, col = r+dr, c+dc
                    if (row < 0 or row >= ROWS or
                       col < 0 or col >= COLS or
                       grid[row][col] != 1):
                        continue
                    queue.append((row,col))
                    grid[row][col]=2
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1















































        # # loop over oranges, and find closest path to an orange, the longest path would be the "min" time for all to rot
        # # this doesn't work because it doesn't account for when the speed of when adjacent oranges are rotting?
        # # if there were more than one rotten oranges, ig the way they spread could be faster than just finding the distance to the closest rotten orange??
        # ROWS, COLS = len(grid), len(grid[0])

        # res = 0
        # rot = defaultdict()

        # def bfs(i,j):
            # queue = deque([(i,j,0)])
            # seen = set()
#
            # while queue:
                # i,j,steps = queue.popleft()
                # if (i < 0 or i >= ROWS or
                    # j < 0 or j >= COLS or
                   # (i,j) in seen or
                   # grid[i][j] == 0):
                    # continue
                # if (i,j) in rot:
                    # return rot[(i,j)] + steps
                # if grid[i][j] == 2:
                    # return steps

                # seen.add((i,j))
                # queue.append((i+1,j,steps+1))
                # queue.append((i-1,j,steps+1))
                # queue.append((i,j+1,steps+1))
                # queue.append((i,j-1,steps+1))
            # return -1
#

        # for i in range(ROWS):
            # for j in range(COLS):
                # if grid[i][j] == 1:
                    # steps = bfs(i,j)
                    # if steps == -1:
                        # return -1
                    # rot[(i,j)] = steps
                    # res = max(res,steps)

        # return res




