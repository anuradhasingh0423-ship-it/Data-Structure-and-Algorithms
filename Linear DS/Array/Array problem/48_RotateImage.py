class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()

if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    print("Original Matrix:")
    for row in mat:
        print(row)
        
    sol.rotate(mat)
    
    print("\nRotated 90 Deg Clockwise:")
    for row in mat:
        print(row)