#here we are going to be given an array in ascending order. The idea is that we need to go through the array and remove the duplicates in place. At the end we return the len of the array. Do not make a new array but rather change the nums array in place. What you will have to return is the len of the unique array.

nums = [1,1,2]

def solution():
    numset = set()
    counter = 0
    for p1 in range(0,len(nums)):
        if nums[p1] not in numset:
            numset.add(nums[p1])
        if nums[p1] in numset:
            nums.pop(p1)
            nums.append(0)
            nums[p
            counter+=1
    countertrue = int(counter/2)
    answer = (len(nums)-countertrue)
    return answer

print(solution())
print(nums)
