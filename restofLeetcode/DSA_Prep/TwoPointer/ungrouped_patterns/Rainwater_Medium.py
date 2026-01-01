"""
Certified Leetcode classic. Capturing the most rainwater. This is a two-pointer problem that you can probobly brute force


"""


class Solution(object):
    def maxArea(self, height):
        # So we can do two pointer here, move the smallest pointer

        # first edge case
        answer = 0

        if not height or len(height) == 1:
            return answer

        l, r = 0, len(height) - 1

        while l <= r:
            # move pointers, capture water
            area = min(height[l], height[r]) * (r - l)
            answer = max(area, answer)

            # move smallest height
            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1

        return answer
