"""
Here we have sepearte squares that we need to calculate the total area of in a y divider line
"""

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        low = 0
        high = 0
        totalArea = 0

        # establish top and bototm of squares for binary range
        for x, y, l in squares:
            totalArea += l * l

            if y < low:
                low = y

            if y + l > high:
                high = y + l

        target = totalArea / 2

        while high - low > .00001:
            mid = (low + high) / 2
            area = 0

            # find area below the current line and calculate area
            for x, y, l in squares:
                if mid <= y:
                    continue
                elif mid >= y + l:
                    area += l * l
                else:
                    area += (mid - y) * l

            # binary search move opinters to move y line down until we get to close
            if area < target:
                low = mid
            else:
                high = mid

        return low