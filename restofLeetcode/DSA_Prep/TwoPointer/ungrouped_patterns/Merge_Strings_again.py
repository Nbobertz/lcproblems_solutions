"""
This is a two pointer problem where we need to merge strings alternativly. The trick is to move pointers and have an and conditional check
"""

#catch edge case of nothing
        ans = ''

        l,r = 0,0

        while l < len(word1) and r < len(word2):
            ans += word1[l]
            ans += word2[r]

            l+=1
            r+=1

        ans = ans+word1[l:]
        ans = ans+word2[l:]

        return ans