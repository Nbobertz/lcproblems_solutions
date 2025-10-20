#here we are going to be given an array of integers. It is our job to return the length of the longest subarray of consecutive integers in the array. The algorith must run in O(n) times= one pass.

#for examle the following array. [100,4,200,1,3,2] will have an answer of 4 since [1,2,3,4] are all in the array.

#constraints: Can there be any negtive numbers in the array? Yes, there can be. Will the array always have numbers in it? Yes, there will always be at least one number. Are the numbers whole? Yes. Can there be repeat numbers? Yes there can.

#brute force. So this is going to be a hashmap problem. We will have to iterate through the hashmap and add each number as the key with the +1 and -1 as the value. During the same loop we will have to look to see if the +1 or -1 values exist in the hashmap as well. If they do then we will have to count and see how many + or - we can go.

#below is example
nums = [9,1,4,7,3,-1,0,5,8,-1,6]

def solution():
    answer = 1
    hmap={}
    l,r = 0,len(nums)-1
    sset=set()
    allsame=set()
    if len(nums)==1:
        return answer
    while l<=r:
        #first iteration is to catch the outlyer where all integer are the same. We use a set and count the len to do this.
        allsame.add(nums[l])
        allsame.add(nums[r])
        #here we add nums[l] pointer to hmap if not found with the inside/outside as values
        if nums[l] not in hmap:
            hmap.update({nums[l]:[nums[l]-1,nums[l]+1]})

        #do same thing for nums[r] if not in hmap
        if nums[r] not in hmap:
            hmap.update({nums[r]:[nums[r]-1,nums[r]+1]})

        #now we are going to see if each point in the hmap' value has a coresponding key, if it does then keep going and add counter to answer. If at anypoint the counter is beaten that becomes counter(answer)

        #iterate pointers by 1 and -1 for l,r
        l+=1
        r-=1
    if len(allsame)==1:
        return answer
    for key in hmap:
        if hmap[key][0] in hmap or hmap[key][1] in hmap:
            sset.add(key)
    answer=len(sset)
    return answer


#I got close but coudnt quite get the hashmap solution figured out. DSA_Prep did it with a Set and it makes much more sense. First turn nums into a set to eliminate all doubles (get's rid of edge cases). Then we make a longest variable. Then we loop through the set and find the first start of the longest subset. Counting forward we then add 1 and store the variable until we hit the end.

def solution2():
    numset=set(nums)
    longest = 0

    for n in nums:
        if (n-1) not in numset:
            length=0
            while (n+length) in numset:
                length +=1
            longest = max(length,longest)

    return longest

print(solution2())