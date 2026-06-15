"""
Here we are testing to see if a string is a palindrom of another
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #if nothing
        if not s:
            return False

        #lower
        s = s.lower() #oN

        #remove everyhing not althanumeric
        tmp = ''
        for x in s:
            if x.isalnum() == True:
                tmp+=x

        if tmp == tmp[::-1]:
            return True

        return False