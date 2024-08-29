#here we are going to be given an array (nums) which will be filled with positive intigers. The idea is to pull out all the integers that corespond with the value integer and then return the len af the array along with the array.

#below is test case
nums = [3,2,2,3]
val = 2
#as we can see above two instances of 3 will be removed and the array will spit back nums = [2,2] with a value of 2.

# I think the best way in going about this is to simply loop through the list and if an integer matches value pull it out. Then return the len of list along with the array

#below is the neetcode way of doing things. Since we don't have to return the array just the total number of items not coresponding to value

def solution():
    k = 0

    for i in range(0,len(nums)):
        if nums[i]!=val:
            nums[k]=nums[i]
            k+=1
    return k
print(solution())