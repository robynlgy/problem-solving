# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # maintain set of seen grids
        # if 1, dfs all the way and add it all up
        # on return compare with max
        # in dfs:
            # base case: if water or seen, return 0
            # dfs all 4 directions, sum them up
            # compare sum with max
            # return sum


        ROWS, COLS = len(grid), len(grid[0])

        maxArea = [0]
        seen = set()

        def dfs(i,j,maxArea):
            if (i < 0 or i>= ROWS or    # i out of bounds
                j < 0 or j >= COLS or   # j out of bounds
                grid[i][j] == 0 or      # water
                (i,j) in seen):         # seen before
                return 0

            seen.add((i,j))
            #just go right and down bcz going up or left means ive alrdy seen it, jk need it all LOL
            sum = 1 + dfs(i,j+1,maxArea) + dfs(i+1,j,maxArea) + dfs(i-1,j,maxArea) + dfs(i,j-1,maxArea)
                        # 1         # 2
            maxArea[0] = max(sum,maxArea[0])
            # print("(",i,j,")",sum)
            return sum




        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    dfs(i,j,maxArea)

        return maxArea[0]