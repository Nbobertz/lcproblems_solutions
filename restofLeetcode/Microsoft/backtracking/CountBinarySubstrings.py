#here we are given a string of 0's and 1's and the idea is that we need to return total number of solutions where the 0's and 1's are the same amount and next to each other respectivly.

s = "00110011"
def solution():
    # we can use backtracking to solve this. Simple subarray with check

    # const your two arrays
    answer = []
    sub = ''  # temp for dfs 'staging' check

    # we are going to use dfs recursivly, capture ALL possible combinations and check while doing so to ensure that it matches criteria.

    def dfs(i, sub):

        # capture our base case
        if i >= len(s):
            answer.append(sub[::])
            return

        # append cur i of s to sub
        sub = sub + s[i]

        # dfs increment by one
        dfs(i + 1, sub)
        # pop to pull back
        sub = sub[:-1]
        # dfs again to capture new int
        dfs(i + 1, sub)

    if not s:
        return 0
    else:
        dfs(0, sub)  # start at the 0 index point on len s

    return answer


def correct():
    class Solution:
        def countBinarySubstrings(self, s: str) -> int:
            # Initialize variables
            pre_len = 0
            cur_len = 1
            count = 0

            # Traverse through the string
            for i in range(1, len(s)):
                # If the current character is the same as the previous character
                if s[i] == s[i - 1]:
                    cur_len += 1
                # If the current character is different from the previous character
                else:
                    pre_len = cur_len
                    cur_len = 1

                # If the previous length is greater than or equal to the current length
                # then we have a valid substring
                if pre_len >= cur_len:
                    count += 1

            # Return the total count of valid substrings
            return count
print(solution())