#here we are given an imput array nums and an integer target. The idea is that we have to write a program to determine if the number is in the array. Also the array is presorted so it is non-descending order.


nums = [-1,0,2,4,6,8]
target = 4


def solution():
    l,r = 0,len(nums)-1
    answer = -1
    while l<=r:
        halfway = int((l+r)/2)
        if nums[halfway]<target:
            l = halfway+1
        if nums[halfway]>target:
            r = halfway-1
        if nums[halfway]==target:
            answer = halfway
            return answer
    return answer

print(solution())