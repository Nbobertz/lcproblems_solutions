"""
Here we are given a preorder traversal and need to figure out how to verify that it exists
The trick is to assign 2 slots per node and then take away a slot if we see a '#'.
This will leave us with a slots == 0 if we have nothing.
If we have slots > 0 or <0 we have a false tree

"""

class Solution(object):
    def isValidSerialization(self, preorder):

        #The trick is to count the slots
        slots = 1
        for node in preorder.split(','):
            slots -= 1
            if slots < 0:
                return False
            if node != '#':
                slots += 2
        if slots == 0:
            return True
        elif slots != 0:
            return False