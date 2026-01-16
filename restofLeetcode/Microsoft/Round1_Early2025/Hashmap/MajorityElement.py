#here we are given an array of nums and the idea is to return the majority element in it.
#a majority elemetn is one where the occurance of that element is greater then the len of nums / 2

nums = [3,2,3]

def solution():
    # here we have to find what the majority element is. We get this by finding any element with a size greater then the len of n divided by 2 using int division.

    # get the delinator of majority element
    majority = len(nums) // 2

    # if len of nums is 1, return nums[0]
    if len(nums) == 1:
        return nums[0]

    # what is len(nums) == 2? will catch edge case of nums = [1,1]
    if len(nums) == 2 and nums[0] == nums[1]:
        return nums[0]
    # going to use a hashmap to keep track and as soon as we get a number larger then the majority we return it
    nummap = {}

    for i in range(0, len(nums)):
        if nums[i] in nummap:
            nummap[nums[i]] += 1
            if nummap[nums[i]] > majority:
                return nums[i]
        elif nums[i] not in nummap:
            nummap[nums[i]] = 1


print(solution())