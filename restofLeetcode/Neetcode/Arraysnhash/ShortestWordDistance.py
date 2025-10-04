#Here we have a lsit of strings and given two words from the list. We need to write a program taht will return teh minimum distance between these two strings.

class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        words = wordsDict

        #o log n

        hm = {}

        for index,word in enumerate(words):
            if word not in hm:
                tmp = [index]
                hm[word]=tmp

            # we found existing word append index
            elif word in hm:
                hm[word].append(index)

        #now we find the shortest distance
        shortest = float('inf')
        arr1 = hm[word1]
        arr2 = hm[word2]

        print(arr1,arr2)

        for ind1 in arr1:
            for ind2 in arr2:
                possible = abs(ind1-ind2)
                shortest = min(possible,shortest)

        return shortest