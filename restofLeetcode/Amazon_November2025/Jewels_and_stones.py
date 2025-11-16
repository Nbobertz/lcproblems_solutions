"""
THe idea here is that you are going to keep track of the total number of jewels and stones that you have.

"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #we can do this in o(n) pass with in operator
        answer = 0

        if not jewels or not stones:
            return answer

        for stone in stones:
            if stone in jewels:
                answer+=1
        return answer