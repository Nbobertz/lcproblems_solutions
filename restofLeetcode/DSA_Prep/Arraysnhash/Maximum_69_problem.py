"""
Here we simply need to replace the first 6 we see in an intgeter with a 9 and call it a day. The idea is that we just need to return the max integer we can see


"""


class Solution(object):
    def maximum69Number(self, num):
        # we can just do this in a o(n) pass
        largest = num

        # convert to string, iterate, convert to num, compare, continue. We got from left to right
        nums = str(num)
        nums = list(nums)
        for n in range(0, len(nums)):
            # check for 9
            if nums[n] == '6':
                # change and convert to 9
                tmp = nums
                tmp[n] = '9'
                tmps = ''.join(tmp)

                # return since the first is always largest
                answer = int(tmps)
                return answer

        return largest