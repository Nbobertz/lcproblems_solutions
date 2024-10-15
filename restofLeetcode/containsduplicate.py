#you are an array (nums) that consists of numbers. Your goal is to loop through this array and determine if each number is distinct

nums = [1,2,3,4]

def solution():
    sset = set()

    for p1 in range(0,len(nums)):
        if nums[p1] in sset:
            answer = True
            return answer
        else:
            sset.add(nums[p1])
    return False


answer = solution()
print(answer)