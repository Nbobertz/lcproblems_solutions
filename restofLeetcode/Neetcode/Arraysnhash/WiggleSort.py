#The idea here is that we are going to iterate through an array and replace an integer if they show up as greater then the previous

class Solution(object):
    def wiggleSort(self, nums):

        #the idea here is that we iterate through the array and swap any posion that is adjacent from each other where the other is larger then the previous. Essentially we are swapping the array like we would a link list

        inc = True
        for i in range(len(nums)-1):
            if inc != (nums[i]<=nums[i+1]):
                nums[i],nums[i+1] = nums[i+1],nums[i]
            inc = not inc


#This is an O(N) solution