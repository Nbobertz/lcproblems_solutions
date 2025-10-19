#loop through an input string, encode it, and the loop through and decode it.

class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for x in strs:
            string = string + "_][][][][][][][][][]_" + x
        return string

    def decode(self, s: str) -> List[str]:
        answer = s.split('_][][][][][][][][][]_')
        answer.pop(0)
        return answer