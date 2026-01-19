"""
Did a microsoft assesment here were the two


"""


class Solution(object):
    def sortColors(self, nums):
        red = 0
        white = 0
        blue = 0

        answer = []

        for n in nums:
            if n == 0:
                red += 1
            elif n == 1:
                white += 1
            elif n == 2:
                blue += 1

        # at o(n) right now
        nn = len(nums)
        count = 0
        for n in range(nn):
            nums.pop()
            if red > 0:
                nums.insert(count, 0)
                red -= 1
            elif white > 0:
                nums.insert(count, 1)
                white -= 1
            elif blue > 0:
                nums.insert(count, 2)
                blue -= 1
            count += 1

        print(nums)
