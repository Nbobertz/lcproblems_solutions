#here we are given an array of integers and we have to determine what the longest consecutive subsequence is.

nums = [100,4,200,1,3,2]

def solution():
    #so the trick here is to convert to a hashset and then loop over that. This problem is literally just do you know what a set is and how to look stuff up in it.

    numset = set(nums)
    longest = 0 #use this to keep track of longest subsequence

    for n in numset:
        if n-1 not in numset: #found the start
            length = 0
            while n+length in numset:
                length+=1
            longest = max(longest,length)

    return longest

print(solution())