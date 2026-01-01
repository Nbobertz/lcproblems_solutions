"""
This is just 3 sum but instead of equaling a target it is smaller. The trick is to sort then do two pinter
"""

# first step, talk through the problem

# step 2. Example inputs and example outputs
# input = [-2,0,1,3]
# output = [-2,0,1], [-2,0,3] = 2

# step3: Claryifing questions
# will the input always be sorted

# step4: edge cases
# is the input sorted, what if no input?
answer = 0
if not nums:
    return answer

nums = sorted(nums)

if len(nums) < 3:
    return answer

l = 0
while l <= len(nums) - 3:
    ll = l + 1
    r = len(nums) - 1

    while ll < r:
        if nums[l] + nums[ll] + nums[r] < target:
            answer += r - ll
            ll += 1
        else:
            r -= 1
    l += 1
return answer



