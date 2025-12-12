"""
Did the first medium DP problem today. Got the intution down which was the most important part. After that it took me a bit of time to nail the solution but I got it
"""


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        import math
        answer = [-math.inf] * len(energy)


        if not energy:
            return answer

        mm = -math.inf

        def jumps(i):
            nonlocal k
            if i >= len(energy):
                return 0

            if answer[i] != -math.inf:
                return answer[i]

            answer[i] = energy[i] + jumps(i+k)
            return answer[i]

        #loop through
        for i,n in enumerate(energy):
            mm = max(mm,jumps(i))
        return mm