# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example 1:
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS, COLS = len(board), len(board[0])

        def capture(i,j):
            if (i < 0 or i >= ROWS or j < 0 or j >= COLS or board[i][j] != 'O'):
                return

            board[i][j] = "T"

            capture(i-1,j)
            capture(i+1,j)
            capture(i,j-1)
            capture(i,j+1)

        # this section can be replaced by code below:
        # for i in range(ROWS):
        #     if board[i][0] == 'O':
        #         capture(i,0)
        #     if board[i][COLS-1] == 'O':
        #         capture(i,COLS-1)
        # for j in range(1,COLS-1):
        #     if board[0][j] == 'O':
        #         capture(0,j)
        #     if board[ROWS-1][j] == 'O':
        #         capture(ROWS-1,j)

        # 1. (DFS) Capture unsurrounded regions (O -> T), only look at border
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        # 3. Uncapture unsurrounded regions (T -> O)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'T':
                    board[i][j] = 'O'







        #slooooowww
        #for each O, go up down left right, return true if reach an X, else false (oob)

#         ROWS, COLS = len(board), len(board[0])
#         flippable = set()
#         not_flippable = set()
#         directions = {
#                  'up':(-1,0),
#                  'down':(1,0),
#                  'left':(0,-1),
#                  'right':(0,1)
#                      }


#         def dfs(i,j,dir):
#             if (i < 0 or i >= ROWS or j < 0 or j >= COLS):
#                 return False

#             if board[i][j] == 'X':
#                 return True

#             r,c = directions[dir]
#             return dfs(i+r,c+j,dir)


#         for i in range(ROWS):
#             for j in range(COLS):
#                 if board[i][j] == 'O':
#                     for dir,(r,c) in directions.items():
#                         if not dfs(i+r,j+c,dir):
#                             not_flippable.add((i,j))
#                             break
#                     if (i,j) not in not_flippable:
#                         flippable.add((i,j))


#         def unflip(i,j,seen):
#             if (i < 0 or i >= ROWS or j < 0 or j >= COLS or
#                 (i,j) in seen or
#                 board[i][j]=="X"): return

#             flippable.discard((i,j))
#             seen.add((i,j))
#             for dir,(r,c) in directions.items():
#                 unflip(i+r,c+j,seen)

#         for (i,j) in not_flippable:
#             for dir,(r,c) in directions.items():
#                 unflip(i+r,j+c,seen=set())


#         for (i,j) in flippable:
#             board[i][j] = 'X'
