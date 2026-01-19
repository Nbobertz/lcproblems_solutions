#here we have the famous 4sum code problem. The idea here is that we have to loop through an array and return all unique combinations that add up to a target number solution.

nums = [1,0,-1,0,-2,2]
target = 0

def solution():
    answer = []
    nums.sort()

    # Iterate through each element, using it as the first number in the sum
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates

        # Now perform 3Sum using two pointers
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue  # Skip duplicates

            l, r = j + 1, len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[j] + nums[l] + nums[r]

                if current_sum == target:
                    answer.append([nums[i], nums[j], nums[l], nums[r]])

                    # Skip duplicates for l and r
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1
                elif current_sum < target:
                    l += 1
                else:
                    r -= 1

    return answer

print(solution())