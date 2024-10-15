#here we are going to be given a string and the idea is that we wan't to find the longest continual substring without duplicate characters.

#This is a sliding window problem because we will take our p1, create a set, and add to the set as we incriment across with p2. If we hit a duplicate we exit out.

s = "aabakd"

def solution():
    charset = set()
    l=0
    res = 0

    for r in range(0,len(s)):
        while s[r] in charset:
            charset.remove(s[l])
            l+=1
        charset.add(s[r])
        res=max(res,r-l+1)
    return res
print(solution())