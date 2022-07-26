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

        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

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

# #   (2,3)

# # [     0   1   2   3   4
# #     ["O","X","X","O","X"],    0
# #     ["X","O","O","X","O"],    1
# #     ["X","O","X","O","X"],    2
# #     ["O","X","O","O","O"],    3
# #     ["X","X","O","X","O"]     4
# # ]

# # [
# #     ["O","X","X","O","X"],
# #     ["X","X","X","X","O"],
# #     ["X","X","X","O","X"],
# #     ["O","X","O","O","O"],
# #     ["X","X","O","X","O"]
# # ]

# # input:
# # [
# #     ["O","X","O","O","X","X"],
# #     ["O","X","X","X","O","X"],
# #     ["X","O","O","X","O","O"],
# #     ["X","O","X","X","X","X"],
# #     ["O","O","X","O","X","X"],
# #     ["X","X","O","O","O","O"]
# # ]

# # expected:
# # [
# #      ["O","X","O","O","X","X"],
# #      ["O","X","X","X","O","X"],
# #      ["X","O","O","X","O","O"],
# #      ["X","O","X","X","X","X"],
# #      ["O","O","X","O","X","X"],
# #      ["X","X","O","O","O","O"]
# # ]

# # output:
# # [
# #     ["O","X","O","O","X","X"],
# #     ["O","X","X","X","O","X"],
# #     ["X","O","X","X","O","O"],
# #     ["X","O","X","X","X","X"],
# #     ["O","O","X","O","X","X"],
# #     ["X","X","O","O","O","O"]
# # ]
