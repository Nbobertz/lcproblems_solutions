"""
Here we are looking for buildings with an ocean view across an array.

[3,2,1] ocean is to right and all buildings have a view since they are larger
"""


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Montomic stack where we have to capture the largest buildings
        if not heights:
            return []

        answer = []

        stack = []

        count = len(heights) - 1
        for n in heights[::-1]:
            i = count
            if not stack:
                stack.append((n, i))
            else:
                if n > stack[-1][0]:
                    # this building is larger, it has an ocean view
                    stack.append((n, i))
                elif n <= stack[-1][0]:
                    # building is same size or smaller, worthless property, just pass
                    pass

            count -= 1

        for build in stack[::-1]:
            answer.append(build[1])
        return answer