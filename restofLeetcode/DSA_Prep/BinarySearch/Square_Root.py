"""
This is for finding the square root of a number
"""

if x < 2:
            return x

        l, r = 1, x // 2
        while l <= r:
            mid = (l + r) // 2
            sq = mid * mid

            if sq == x:
                return mid
            elif sq < x:
                l = mid + 1
            else:
                r = mid - 1

        return r