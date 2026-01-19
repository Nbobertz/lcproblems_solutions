"""
THis is two find letter case permutations
"""

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        if not s:
            return answer

        def dfs(i,cur):
            #i = index, cur = arry we working on
            if i>= len(s):
                tmp = ''.join(cur)
                answer.append(tmp)
                return

            if s[i].isalpha() == True:
                cur.append(s[i].lower())
            elif s[i].isalpha() != True:
                cur.append(s[i])
            dfs(i+1,cur)
            cur.pop()
            if s[i].isalpha() == True:
                cur.append(s[i].upper())
            elif s[i].isalpha() != True:
                cur.append(s[i])
            dfs(i+1,cur)
            return