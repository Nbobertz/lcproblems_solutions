"""
Reconstruct the IP from a series of integers
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []

        def is_valid(s):
            temp = s.split('.')

            if len(temp[-1]) > 3:
                return

            for val in temp:
                if val == '':
                    return

                if len(val) > 1 and val[0] == '0':
                    return

                if int(val) > 255:
                    return
            answer.append(s)

        def dfs(prev_part, count, s):
            if (count == 3):
                is_valid(prev_part + s)
                return
            for i in range(1, 4):
                dfs(prev_part + s[:i] + '.', count + 1, s[i:])

        dfs('', 0, s)
        return answer