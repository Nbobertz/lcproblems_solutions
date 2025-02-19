#insert

def solution():
    numset = set()
    counter = 0
    for p1 in range(0, len(nums)):
        if nums[p1] not in numset:
            numset.add(nums[p1])
        if nums[p1] in numset:
            nums.pop(p1)
            nums.append(0)
            counter += 1
    answer = (len(nums) - int(counter / 2))
    return answer

def realsol():
    i = 1

    for j in range(1, len(nums)):
        if nums[j] != nums[i - 1]:
            nums[i] = nums[j]
            i += 1

    return i