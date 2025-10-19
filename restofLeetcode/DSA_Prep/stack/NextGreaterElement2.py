#here we have an array and are looking for the next greater element in a ciruclar array.
#I tried the two pointer solution but it did not work on teh halfway point.
class Solution(object):
    def nextGreaterElements(self, nums):
        # capture both index and element
        answer = []
        for p1 in range(0, len(nums)):
            index = p1
            if p1 == 0:
                for p2 in range(p1 + 1, len(nums)):
                    found = False
                    if nums[p1] < nums[p2]:
                        found = True
                        answer.append(nums[p2])
                        break
                    if found == False:
                        answer.append(-1)
                        break

            elif p1 != 0 and p1 != len(nums):
                # anything but o index
                found = False
                # look to right
                for p2 in range(p1 + 1, len(nums)):
                    if nums[p1] < nums[p2]:
                        found = True
                        answer.append(nums[p2])
                        break
                # look to left
                for p2 in range(0, p1):
                    if nums[p1] < nums[p2]:
                        found = True
                        answer.append(nums[p2])
                        break
                if found == False:
                    answer.append(-1)
                    continue
            elif p1 == len(nums):
                # look from 0,p1
                for p2 in range(0, p1):
                    found = False
                    if nums[p1] < nums[p2]:
                        found = True
                        answer.append(nums[p2])
                        break
                    if found == False:
                        answer.append(-1)

            # else:
            #     #found nothing bigger
            #     answer.append(-1)

        return answer

#here is how we do this by doubling up the input array
    def solution(self,nums):
        #we double up the array, then simply go left to right
        dnums = nums + nums

        answer = []

        if len(nums) == 0:
            return []
        elif len(nums)==1:
            return [-1]

        for p1 in range(0,len(nums)):
            p2 = p1+1
            while p2 != len(dnums)-1:
                if nums[p1]<dnums[p2]:
                    answer.append(dnums[p2])
                    break

                elif p2 == len(dnums)-2:
                    answer.append(-1)
                    break
                p2+=1
        return answer