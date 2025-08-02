#legendary 3 sum problem, you need ot find valid triples where the elements sum to 0 and the index points are unique.

nums = [1,2,3,4,5,-5,-4,-2,-1]



class Solution(object):
    def threeSum(self, nums):
        answer = []
        nums.sort()

        for p1 in range(0, len(nums) - 2):
            # Skip duplicates for the first element
            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                continue

            # If current number is > 0, break early (since array is sorted)
            if nums[p1] > 0:
                break

            l, r = p1 + 1, len(nums) - 1

            while l < r:
                total = nums[p1] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    triplet = [nums[p1], nums[l], nums[r]]
                    if triplet not in answer:
                        answer.append(triplet)

                    # Move both pointers and skip duplicates
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return answer