#here we are given an integer array and asked to print the next integer that is larger than it to it's right. If none exists then we print -1.


#this was asked in my microsoft interview. I came up with the brute force approach.

nums = [1,5,2,6,7,8,1,9]


def solution():
    #two pointer solution
    for i in range(0,len(nums)):
        if i == len(nums)-1:
            print("{a} -> {b}".format(a=nums[i],b=-1))
            break
        for j in range(i+1,len(nums)):
            if nums[i]<nums[j]: #found a higher number
                print("{a} -> {b}".format(a=nums[i], b=nums[j]))
                break
            elif j == len(nums)-1:
                print("{a} -> {b}".format(a=nums[i], b=-1))
                break

print(solution())