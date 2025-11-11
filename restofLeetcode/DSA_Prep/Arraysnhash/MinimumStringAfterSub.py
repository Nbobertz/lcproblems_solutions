"""
Here we just constantly remove characters until they are no longer in the string and then return the strings length


"""

class Solution:
    def minLength(self, s: str) -> int:
        #we can do this with just a while loop, just continously check
        while 'AB' in s or 'CD' in s:
            if 'AB' in s:
                s=s.replace('AB','')
            elif 'CD' in s:
                s=s.replace('CD','')
        return len(s)