"""
Here we are just seeing if a moving robot will return to origin
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        #we can simulate this in o(n) via a hashmap and just splitting the string and then going through it

        if not moves:
            #return true as we end up where we start at 0,0
            return True

        hm = {
            'U':[1,0],
            'D':[-1,0],
            'L':[0,-1],
            'R':[0,1]
        }

        moves = list(moves)
        pos,start = [0,0],[0,0]

        #o(n) pass
        for mov in moves:
            if mov in hm:
                lat,log = pos[0],pos[1]
                lat = lat+hm[mov][0]
                log = log+hm[mov][1]
                pos = [lat,log]
            else:
                print('Not a valid move')

        if pos == start:
            return True
        elif pos != start:
            return False



