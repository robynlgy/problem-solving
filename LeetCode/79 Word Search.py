# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r,c,i):
            if i == len(word): return True

            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != word[i] or
                (r,c) in path):
                return False

            path.add((r,c))
            res = (dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1) or
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1))
            path.remove((r,c))
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True

        return False
# ================================================================================
#         # using an array also works
#         used = []

#         def dfs(r,c,i):
#             if i == len(word): return True

#             if (r < 0 or c < 0 or
#                 r >= ROWS or c >= COLS or
#                 board[r][c] != word[i] or
#                 (r,c) in used):
#                 return False

#             used.append((r,c))
#             if ((dfs(r, c+1, i+1) or
#                 dfs(r, c-1, i+1) or
#                 dfs(r+1, c, i+1) or
#                 dfs(r-1, c, i+1))):
#                 return True

#             used.pop()
#             return False



#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if dfs(i,j,0):
#                     return True

#         return False



        # start at 0,0
        # if matches first word letter, go to next step
            # move up/down/left/right if valid,
            # recurse with the next step and letter, if eventually reads true then return true
            # else look at another direction
        # have a set of coords for letters cells seen

# too slow w helper fx:
#         used = []

#         def dfs(r,c,i,used):
#             l = word[i]
#             used.append((r,c))
#             if l == board[r][c]:
#                 if i == len(word)-1: return True

                # for dir in self.next_steps(board, r, c):
                #     dr,dc = dir
                #     if (dr,dc) not in used and dfs(dr,dc,i+1,used):
                #         return True
#             if used: used.pop()
#             return False

#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if dfs(i,j,0,used):
#                     return True

#         return False



#     def next_steps(self,board,r,c):
#         res = []
#         directions = [(0,1),(-1,0),(0,-1),(1,0)]

#         for dir in directions:
#                 dr,dc = dir
#                 dr += r
#                 dc += c
#                 # if dr >= 0 and dr < len(board) and dc>=0 and dc<len(board[0]):
#                 res.append((dr,dc))

#         return res







