#here we are going to be given an array and an integer. The integer represents the maximum length of a window. The idea is that this window starts at hte left most side of the array and will loop over the array until the right side of the window hits the end of the array. We will have to capture the maximum value of this window at each iteration and return that as an array.

nums = [1,2,1,0,4,2,6]
k=3

def solution():
    if k>len(nums):
        return False
    l,r = 0,k
    answer = []


    #now we loop through the array by one and return the maximum value from that window into an array
    while r<=len(nums):
        initm = nums[l]
        for p1 in range(l,r):
            num = nums[p1]
            maxim=max(num,initm)
            initm=maxim
        answer.append(maxim)
        l+=1
        r+=1
    return answer

#my solution ran in o(n(k-n)) time and did not pass all edge cases. Still a win though because I did it on my own.
#neetcode's solution. use a deque that always checks. We only have to loop throgh all numbers once as we add them to the que. This works because we add one number at a time and then check to see if it is bigger. If it is then we add that number to answer if it is not then we add the previous number.

def solution2():
    import collections
    output =[]
    q = collections.deque()
    l=r=0

    while r< len(nums):
        while q and nums[q[-1]]<nums[r]:
            q.pop()
        q.append(r)

        if l> q[0]:
            q.popleft()
        if (r+1) >=k:
            output.append(nums[q[0]])
            l+=1
        r+=1
    return output

print(solution2())