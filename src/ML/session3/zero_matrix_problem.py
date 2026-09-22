class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Set entire rows and columns to zero if any cell contains zero.

        The solution modifies the matrix in place and uses the first row
        and first column as markers, achieving O(1) extra space.

        Args:
            matrix (List[List[int]]): The input matrix to modify.

        Returns:
            None: The matrix is modified in place.
        """
        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if the first row contains zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Check if the first column contains zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True

        # Use the first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to zero based on the markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s= Solution()
s.setZeroes(matrix)
print(matrix)