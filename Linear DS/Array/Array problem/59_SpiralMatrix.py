class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1
            
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1
            
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1
                
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1
                
        return res

if __name__ == "__main__":
    sol = Solution()
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    
    print("-" * 50)
    print(f"Test 1 (3x3): {sol.spiralOrder(m1)}")
    print(f"Test 2 (3x4): {sol.spiralOrder(m2)}")
    print("-" * 50)