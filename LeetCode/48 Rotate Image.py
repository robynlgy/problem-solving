# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO Nclass Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # n x n matrix
        left, right = 0, len(matrix)-1
        top, bottom = left, right

        while left<right and top<bottom:

            for i in range(right - left):
                top_left = matrix[top][left + i]

                # bottom-left to top-left
                matrix[top][left + i] = matrix[bottom - i][left]

                #bottom-right to bottom-left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                #top-right to bottom-right
                matrix[bottom][right - i] = matrix[top + i][right]

                #top-left to top-right
                matrix[top + i][right] = top_left
            left += 1
            right -= 1
            top += 1
            bottom -= 1





