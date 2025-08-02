#here we are going to group all the aski values together and then return the integer value into a hashmap. The idea is that if the aski values are the same it's an anagram
#kinda like bitwise solution
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord("a")] +=1
            res[tuple(count)].append(s)
        return list(res.values())
