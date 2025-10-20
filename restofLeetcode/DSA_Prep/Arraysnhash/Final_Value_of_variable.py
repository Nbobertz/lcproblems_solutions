"""
This one is pretty simple, we just need to build a map and then perform a series of operations on an array of characters.

I did this with a hashmap much like two-sum

"""

class Solution(object):
    def finalValueAfterOperations(self, operations):
        #here we simply need to do a o(n) pass and return final value

        X = 0

        #build a map for easy lookup
        hm = {
            "++X":1,
            "X++":1,
            "--X":-1,
            "X--":-1
        }

        for op in operations:
            num = hm[op]
            X = X+num

        return X