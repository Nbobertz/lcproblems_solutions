#here we are going to be given a string and integer. The idea is that you can take the integer and build any continous string of characters by changing the integer value.

#So this is a sliding window problem. The idea is that you go from left to right and then when you hit the end you can replace the -1 pointer position if it's diffrent. This way you can use your replacements to change the longest string.

s = "XYYX"
k = 2

def solution():
    #construct the longest variable
    longest =0

    #now we construct the left and right pointer. 0 and 1 pointer because we are going to move right pointer until we see a diffrent letter. If we do we can add two to the longest. The idea is that we don't even have to change the letter; only the number
    l,r = 0,1
    while l<len(s):
        tmplong = k
        while s[l]==s[r]:
            print(s[r])
            tmplong+=1
            r=r+1
            print(r)
            if r==l:
                break
            if r==len(s)-1:
                r=0
        if s[l]!=s[r]:
            l=r
            r+=1
            longest=max(tmplong,longest)
        l+=1
    return longest


#had to look up the neetcode solution. My idea of looping around did not work because the loop would break all the time.

def solution2():
    count = {}
    res = 0

    l=0
    maxf=0

    for r in range(len(s)):
        count[s[r]]= 1 + count.get(s[r],0)
        maxf = max(maxf,count[s[r]])

        while (r-l+1)-maxf>k:
            count[s[l]]-=1
            l+=1
        res = max(res,r-l+1)
    return res
answer = solution2()
print(answer)
