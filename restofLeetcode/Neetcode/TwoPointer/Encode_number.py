#here the idea is that we will recieve an array and have to encode each number and then add them together.

class Solution(object):
    def sumOfEncryptedInt(self, nums):
        # find the largest integer in the nums array
        # so the idea is that for each string we simply iterate through and figure out what the max integer is

        # this is an o(n2) solution that is brute force. I am sure we can use a hashmap.

        answer = 0
        tmp_arr = []

        # edge case of no nums or nums len ==1
        if not nums:
            return 0

        for p1 in range(0, len(nums)):
            max_num = 0
            tmp_s = ''

            snum = str(nums[p1])
            for char in snum:
                if int(char) >= max_num:
                    max_num = int(char)
            for x in range(0, len(snum)):
                tmp_s = tmp_s + str(max_num)
            tmp_arr.append(int(tmp_s))

        for num in tmp_arr:
            answer += int(num)
        return answer




