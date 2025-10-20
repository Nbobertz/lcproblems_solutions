#valid again

class Solution(object):
    def isPalindrome(self, s):
        l,r = 0,len(s)-1

        while l < r:
            #while loop to move pointers past noalnum
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1

            #we are at alnum chars, compare
            if s[l].lower() != s[r].lower():
                return False

            l+=1
            r-=1
        return True