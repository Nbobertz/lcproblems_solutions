#here we are going to be given two strings. We are to grab all characters with their count from the first string and then loop through and see if all words are used excactly once in the next word. If we run through the entire hashmap
#then we have reached the end of the word and found a hashmap.

class Solution:
    def prob_sol(s,t):
        # here we can loop through this and add each character to a hashmap on the first loop.
        # then we can easily loop through the second word and remove a letter. If the letter
        # equals 0 we pop from hm

        hm = {}

        # capture edge case of if the len of both words is not the same
        if len(s) != len(t):
            return False

        for char in s:
            if char not in hm:
                hm[char] = 1
            elif char in hm:
                hm[char] += 1

        # loop through second word
        for char in t:

            # captures if the letter is not in hashmap
            if char not in hm:
                return False

            elif char in hm:
                hm[char] -= 1
                if hm[char] == 0:
                    hm.pop(char)

        return True

s = 'nick'
t = 'kcin'


a = Solution.prob_sol(s,t)
print(a)