from typing import List


class Solution:
    def spiralOrder(self, matrix:[[int]]) -> [int]:
        if not matrix:
            return []

        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1 
        res = []

        while True:
            for i in range(l, r + 1):
                # left to right
                res.append(matrix[t][i])
            t += 1 
            if t > b:
                break   

            for i in range(t, b+1):
                # top to bottom
                res.append(matrix[i][r])
            r -= 1 
            if r < l:
                break 
            
            for i in range(r, l-1, -1):
                # right to left
                res.append(matrix[b][i])
            b -= 1
            if b < t:
                break 
                
            for i in range(b, t-1, -1):
                # bottom to top
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break 

        return res

if __name__ == '__main__':
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # matrix = [[1], [2], [3]]
    matrix = [[2, 5, 8], [4, 0, -1]]
    print(Solution().spiralOrder(matrix))

