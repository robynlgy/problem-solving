# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

#Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS , COLS = len(grid), len(grid[0])
        seen = set()
        count = 0

        def dfs(i,j):
            if (i < 0 or i>= ROWS or
                j < 0 or j>= COLS or
                (i,j) in seen or
                grid[i][j] == '0'):
                return False

            seen.add((i,j))
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            return True

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j):
                    count += 1

        return count

#         count = 0

#         def dfs(r,c):
#             # print("beg",r,c)
#             # note: instead of mutating grid, could implement a seen set passing in coords
#             grid[r][c] = '#'
#             directions = [[-1,0],[1,0],[0,-1],[0,1]]
#             for dr, dc in directions:
#                 _r = r + dr
#                 _c = c + dc
#                 # print("next",_r,_c)
#                 if (_r in range(len(grid)) and
#                     _c in range(len(grid[0])) and
#                     grid[_r][_c] == '1'):
#                     dfs(_r,_c)

#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == '1':
#                     dfs(r,c)
#                     count += 1
#         return count




# makes adjacnecy list, similar idea?

#         count = 0
#         graph = self.makeGraph(grid)

#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j] == "1":
#                     coord = (i,j)
#                     if self.dfs(coord,graph,grid):
#                         count+=1

#         # print(grid)
#         return count

#     def dfs(self,coord,graph,grid):
#         x,y = coord
#         if grid[x][y]=="#" or grid[x][y]=="0": return False

#         grid[x][y]="#"
#         for neighbor in graph[coord]:
#             self.dfs(neighbor,graph,grid)
#         return True


#     def makeGraph(self,grid):
#         res = defaultdict(list)

#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 x = (i,j)
#                 if i>0: res[x].append((i-1,j))
#                 if i<len(grid)-1: res[x].append((i+1,j))
#                 if j>0: res[x].append((i,j-1))
#                 if j<len(grid[i])-1: res[x].append((i,j+1))

#         return res