# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # alternative: initialize as defaultdict(set) instead of arrays
        # the key for grid could be a tuple instead eg. (1,1) for middle grid, (0,0) for first grid

        row = [[] for i in range(9)]
        col = [[] for i in range(9)]
        grid = [[] for i in range(9)]

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell != '.':
                    g = (r//3)*3+(c//3)
                    if cell in row[r] or cell in col[c] or cell in grid[g]:
                        return False
                    else:
                        row[r].append(cell)
                        col[c].append(cell)
                        grid[g].append(cell)

#         print("row",row)
#         print("col",col)
#         print("grid",grid)

        return True




