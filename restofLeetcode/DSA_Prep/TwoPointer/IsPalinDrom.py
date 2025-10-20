#Did the string palindrom problem. Pretty easy.

class Solution(object):
    def isPalindrome(self, s):
        l,r = 0,len(s)-1
        while l<=r:
            lc,rc = s[l].lower(),s[r].lower()
            if lc.isalnum() == False or lc == ' ':
                l+=1
                continue
            if rc.isalnum() == False or rc == ' ':
                r-=1
                continue
            if lc!=rc:
                print(rc.isalnum())
                print(lc,rc)
                return False
            l+=1
            r-=1
        return True