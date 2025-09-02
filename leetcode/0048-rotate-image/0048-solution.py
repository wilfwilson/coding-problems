class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)

        # 90º clockwise rotation is the same as transpose + vertical reflection.

        # So first transpose the matrix.
        for i in range(n - 1):
            for j in range(i + 1, n):
                x = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = x

        # And then reverse each row.
        for i in range(n):
            matrix[i] = matrix[i][::-1]
