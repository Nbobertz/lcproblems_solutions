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
    while l<=r:
        #we add the element with the index point
        hmap.update({l:nums[l]})
        hmap.update({r:nums[r]})
        l+=1
        r-=1

    #now we are going to loop through the hashmap and remove all key's which together add up to 0:

    for p1 in range(0,len(hmap)):
        for p2 in range(p1+1,len(hmap)):
            for p3 in range(p2+1,len(hmap)):
                if hmap[p1]+hmap[p2]+hmap[p3] == 0:
                    answer.append([hmap[p1],hmap[p2],hmap[p3]])
                    hmap['test']=hmap[p1]
                    del hmap[p1]
                    hmap['test']=hmap[p2]
                    del hmap[p2]
                    hmap['test']=hmap[p3]
                    del hmap[p3]
    #couldnt get it right on the first try. Continued to have problems with the pointer enumeration

    return answer



#below is neetcode's code. The above code I could not edit the dictionary in place. DSA_Prep just changed the a variable and sorted the list ahead of time.
def solution2():
    res = []
    nums.sort()

    for i,a in enumerate(nums):
        if i>0 and a==nums[i-1]:
            continue

        l,r = i+1,len(nums)-1
        while l<r:
            thresum = a+nums[l]+nums[r]
            if thresum>0:
                r-=1
            elif thresum<0:
                l+=1
            else:
                res.append([a,nums[l],nums[r]])
                l+=1
                while nums[l]==nums[l-1] and l<r:
                    l+=1
    return res
print(solution2())