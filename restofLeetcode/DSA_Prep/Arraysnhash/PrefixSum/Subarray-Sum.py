"""
This is a prefix sum problem. Goign to do nothing but prefix sum stuff to get a hang of it today
"""
def solution(nums,k):
    ans = 0

    if not nums:
        return ans

    cursum = 0
    prefix = {0: 1}

    for n in nums:
        cursum += n

        diff = cursum - k

        if diff in prefix:
            ans += prefix[diff]

        if cursum in prefix:
            prefix[cursum] += 1
        else:
            prefix[cursum] = 1

    return ans