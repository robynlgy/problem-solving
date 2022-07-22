There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #how do i know im in pacific/atlantic
        # pacific:  r < 0 or c < 0
        # atlantic:  r >= ROWS or c >= COLS

        ROWS, COLS = len(heights), len(heights[0])
        res = []
        pac, atl = set(), set()
        seen = set()

        def dfs(i, j, visit, prev):
            if ((i,j) in visit or
                i<0 or j <0 or i>= ROWS or j >= COLS or
                heights[i][j]<prev ):
                return

            visit.add((i,j))

            dfs(i+1,j,visit,heights[i][j])
            dfs(i-1,j,visit,heights[i][j])
            dfs(i,j+1,visit,heights[i][j])
            dfs(i,j-1,visit,heights[i][j])


        for j in range(COLS):
            dfs(0, j, pac, heights[0][j])
            dfs(ROWS-1, j, atl, heights[ROWS-1][j])

        for i in range(ROWS):
            dfs(i,0, pac, heights[i][0])
            dfs(i,COLS-1, atl, heights[i][COLS-1])

        return list(pac.intersection(atl))