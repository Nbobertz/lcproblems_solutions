"""
Here we are simply scanning through array and popping all anagrams of the word

https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/solutions/7272204/easy-python-reduction-by-algorithmus-97nw/
"""


class Solution(object):
    def removeAnagrams(self, words):
        # just do a o(n) pass from +1 and check to see if it's an anagram

        answer = []

        l = 1
        while l <= len(words) - 1:
            # o(logn)
            # check behind if anagram
            word_r = list(words[l])
            word_l = list(words[l - 1])

            # turn into sorted
            word_r.sort()
            word_l.sort()

            # turn into strings
            wordr = "".join(word_r)
            wordl = "".join(word_l)

            # logic to delete word r
            if wordr == wordl:
                # delete word r
                tmp = words[l]
                words.remove(tmp)
                l = 1

                # if we pop down to just 1 word
                if len(words) <= 1:
                    answer.append(words[0])
                    return answer

            # move pointer
            elif wordr != wordl:
                l += 1

        return words