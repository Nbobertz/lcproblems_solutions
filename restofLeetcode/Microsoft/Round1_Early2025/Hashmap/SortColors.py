#here we are given an array and asked to sort it in place. Only 0,1,2 can be in the input array.


nums = [2,0,2,1,1,0]


def solution():
    # sort in place
    # 0 = red
    # 1 = white
    # 2 = blue

    # for this we can use a hashmap. We only know there will ever be 0,1,2 in the array. So we loop through and add that to a hashmap. From this we then simply append, decrement hashmap, and keep counter for the current index.

    hm = {}

    for i in range(0, len(nums)):
        if nums[i] not in hm:
            hm[nums[i]] = 1
        elif nums[i] in hm:
            hm[nums[i]] += 1

    # edit in place
    counter = 0
    while 0 in hm and hm[0] != 0:
        nums[counter] = 0
        hm[0] -= 1
        counter += 1
    while 1 in hm and hm[1] != 0:
        nums[counter] = 1
        hm[1] -= 1
        counter += 1
    while 2 in hm and hm[2] != 0:
        nums[counter] = 2
        hm[2] -= 1
        counter += 1
solution()
print(nums)