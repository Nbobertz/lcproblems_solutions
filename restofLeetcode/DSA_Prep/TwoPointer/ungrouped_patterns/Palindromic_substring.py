class Solution(object):
    def longestPalindrome(self, s):
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        longest = ''
        for i in range(len(s)):
            # Odd length
            tmp1 = expandAroundCenter(i, i)
            # Even length
            tmp2 = expandAroundCenter(i, i+1)
            # Update longest
            if len(tmp1) > len(longest):
                longest = tmp1
            if len(tmp2) > len(longest):
                longest = tmp2

        return longest