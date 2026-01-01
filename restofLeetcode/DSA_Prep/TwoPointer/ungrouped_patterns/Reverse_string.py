"""
Here we are simply reversing a string as we iterate over it. Pretty simple problem that i did first try in under 2 minutes

"""

class Solution(object):
    def reverseString(self, s):
        if len(s) == 1:
            return s
        elif len(s) == 2:
            s[0],s[1] = s[1],s[0]
            return s

        #I guess we can try substitution
        l,r = 0,len(s)-1
        while l<=r:
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
        return s