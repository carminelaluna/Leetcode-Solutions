class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        row0 = [False] * m
        col0 = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row0[i] = True
                    col0[j] = True
        for i in range(m):
            for j in range(n):
                if row0[i] or col0[j]:
                    matrix[i][j] = 0
        return matrix
            
