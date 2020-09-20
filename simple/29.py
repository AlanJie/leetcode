from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows = len(matrix)
        if not rows:
            return []
        cols = len(matrix[0])
        if not cols:
            return []

        print(rows)

        res = []

        left, right, top, bottom = 0, cols-1, 0, rows-1

        if cols == 1:
            return matrix[0]

        if rows == 1:
            for i in range(rows):
                res.extend(matrix[i])

                return res
        
        while top <= bottom and left <= right:
            if left == right and top == bottom:
                res.append(matrix[left][top])
            
            for i in range(left, right):
                res.append(matrix[top][i])
            
            for i in range(top, bottom):
                res.append(matrix[i][right])
            
            for i in range(right, left, -1):
                res.append(matrix[bottom][i])

            for i in range(bottom, top, -1):
                res.append(matrix[i][left])

            left += 1 
            right -= 1 
            top += 1 
            bottom -= 1 

        return res 


if __name__ == '__main__':
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    matrix = [[1], [2], [3]]
    print(Solution().spiralOrder(matrix))

