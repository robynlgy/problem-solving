# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# #
# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search for the largest value less than target
            # compare first val of each row:
                # if larger, hi = med
                # if smaller, lo = med + 1
        rlo,rhi = 0, len(matrix)

        while rlo < rhi:
            rmed = (rlo + rhi)//2
            if target < matrix[rmed][0]:
                rhi = rmed
            elif target >= matrix[rmed][0]:
                rlo = rmed + 1
        row = matrix[rlo-1]

        l,r = 0,len(row)-1

        while l <= r:
            m = (l+r)//2
            if target < row[m]:
                r = m - 1
            elif target > row[m]:
                l = m + 1
            else:
                return True

        return False