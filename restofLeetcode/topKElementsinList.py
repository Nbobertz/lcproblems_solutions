#Given an integer array nums and an integer k, return the k most frequent elements within the array.

#The test cases are generated such that the answer is always unique.

#You may return the output in any order.

#here we are going to be given an array (nums) and an integer (k) the goal here is to find the k most freqent elements in the array.


#constraints
#any negative numbers? Yes. Can K be larger then the len of the array? No.

#example
nums = [4,1,-1,2,-1,2,3]
k=2

def solution():
    hmap={}
    answer = []
    l,r = 0,len(nums)-1

    if len(nums)==1:
        answer.append(nums[0])
        return answer

    #now we add iterate through array, add to hmap with number of times it is hit.
    while l<=r:
        if nums[l] in hmap:
            hmap[nums[l]]+=1
        elif nums[l] not in hmap:
            hmap.update({nums[l]:1})
        if nums[r] in hmap:
            hmap[nums[r]]+=1
        elif nums[r] not in hmap:
            hmap.update({nums[r]:1})
        l+=1
        r-=1

    #now we sort the hashmap in ascending order and assign to list
    sorted_hash = dict(sorted(hmap.items(),key=lambda item:item[1],reverse=True))
    limap=list(sorted_hash)

    #now we add to answer array based off k value. Our array is sorted in descending order.
    for p1 in range(0,k):
        answer.append(limap[p1])
    return answer

print(solution())

