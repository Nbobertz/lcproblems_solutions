#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

#only use constant extra space

#So the goal here is that we are going to be given an array of integers. This array will be 1 indexed so instead of starting at the 0 point we will start at the 1 point. After this we will be given another inegeter assigned to variable target. We will loop through the array and see if there is any two integers that add up to our target.

#we can always just do two pointer and then return the answer. This is not the most efficent way to go about this but it gets the job done.

numbers = [-1,0]
target = -1

#below is solution
def solution():
    answer = []
    hmap={}
    l,r = 0,len(numbers)-1
    if len(numbers)==2:
        answer.append(1)
        answer.append(2)
        return answer
    while l<r:
        if numbers[l] not in hmap:
            hmap.update({numbers[l]:l})
        if numbers[r] not in hmap:
            hmap.update({numbers[r]:r})
        t2 = target-numbers[l]
        t3 = target-numbers[r]
        if t2 in hmap:
            answer.append(l+1)
            answer.append(hmap[t2]+1)
            answer=sorted(answer)
            if hmap[t2]!=l+1:
                finalanswer = []
                finalanswer.append(answer[0])
                finalanswer.append(answer[1])
                return finalanswer
        elif t3 in hmap:
            answer.append(r+1)
            answer.append(hmap[t3]+1)
            answer=sorted(answer)
            if hmap[t3]+1!=r+1:
                finalanswer = []
                finalanswer.append(answer[0])
                finalanswer.append(answer[1])
                return finalanswer
        l+=1
        r-=1

#the problem lied. they gave me an edge case with the same element used twice ...

#here is neetcode's solution
def solution2():
    l,r = 0,len(numbers)-1
    while l<r:
        curSum = numbers[l]+numbers[r]

        if curSum>target:
            r-=1
        elif curSum<target:
            l+=1
        else:
            return [l+1,r+1]

print(solution())
print(solution2())