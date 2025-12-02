"""
This is just a o(n) walk around a matrix
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []

        if not matrix:
            return answer

        n = len(matrix) #rows
        m = len(matrix[0]) #cols

        top = 0
        bottom = n-1
        left = 0
        right = m-1

        #we step in as we go over the array
        while top <= bottom and left <= right:
            for i in range(left,right+1):
                answer.append(matrix[top][i])
            top += 1

            for i in range(top,bottom+1):
                answer.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right,left-1,-1):
                    answer.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom,top -1, -1):
                    answer.append(matrix[i][left])
                left+=1
        return answer