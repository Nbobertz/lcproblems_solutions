"""
Here we are checking to see if a number is a happy number meaning that it can be squared continously until it hits 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        if not n:
            return False

        def loop(n):
            st = str(n)
            tmp = 0
            for char in st:
                tmp += (int(char) ** 2)
            return tmp

        ss = set()  # stores seen numbers
        while n not in ss:
            ss.add(n)
            n = loop(n)
            if n == 1:
                return True
        return False
