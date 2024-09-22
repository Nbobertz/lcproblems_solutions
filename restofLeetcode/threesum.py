#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

#the output can't contain any duplicate triplets.

#brute force. So the best way I think to go about this would be a combonation of a hashmap along with two pointer. We will have the pointers at left and right. And with each iteration have the pointers move to the left. After this have all the combos that equal 0 be printed out into an answer array. Only have distinct combos be added to the answer array. Each number can only be used once

nums = [-1,0,1,2,-1,-4]
target = 0

def solution():
    answer = []
    hmap={}
    l,r = 0,len(nums)-1

    #now we loop through the array and add to the hmap dict
    while l<r:
        #we add the element with the index point
        hmap.update({nums[l]:l})
        hmap.update({nums[r]:r})