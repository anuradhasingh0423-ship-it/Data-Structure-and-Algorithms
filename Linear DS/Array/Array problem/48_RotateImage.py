class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()

if __name__ == "__main__":
    sol = Solution()
    
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Original 1:")
    for row in m1:
        print(row)
        
    sol.rotate(m1)
    
    print("\nRotated 90° Clockwise 1:")
    for row in m1:
        print(row)