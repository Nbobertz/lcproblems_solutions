#if the array cointains duplicate itegers return False else return True

nums = [1,2,3,4,5,6]

def solution():
    sset=set()
    answer = False
    l,r = 0,len(nums)
    while l<r:
        print(l)
        print(nums[l])
        print(nums[r-1])
        print(r)
        if l!=0 and nums[l] or nums[r-1] in sset:
            answer = True
            return answer
        if nums[l] not in sset:
            sset.add(nums[l])
        if nums[r-1] not in sset:
            sset.add(nums[r-1])
        l += 1
        r = r-1
    return answer


answer = solution()
print(answer)