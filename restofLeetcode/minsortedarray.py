#here we are going to be given a random array that is presorted and rotated to the right. The idea here is that you will need to find the minimim number in the array in o log n. Calling min on the array is on.

nums = [4,5,6,7,0,1,2]

def solution():
    #so the idea here is that we call the half annd see if hte nnumber to the right or left is greater then run logic off that

    l,r = 0,len(nums)-1

    #captures base case
    if len(nums)==1:
        return nums[0]

    #if last element is greater thenn first element then there is no rotation
    if nums[r] > nums[0]:
        return nums[0]

    #binary search
    while l <= r:
        half = int((l+r)/2)

        #if half is greater then its next elment then mid +1 is the answer
        if nums[half]>nums[half + 1]:
            return nums[half+1]

        #if the mid element is lesser then its previous element then the mid element is the smmallest
        if nums[half]<nums[half-1]:
            return nums[half]

        #if the mid element value is greater then the 0th element that means the least value is still somewhere to the right
        if nums[half] > nums[0]:
            l = half +1

        #if nums[0] greater then mid value that means the smallest is to the left
        else:
            r = half -1
print(solution())