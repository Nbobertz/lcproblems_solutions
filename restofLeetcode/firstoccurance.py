#here we are going to be given a string of random characters/words. The string is 'haystack' and the goal is to see if a substring exists within this string. The substring is titled 'needle.' Return the index of the first index this substring occures at.

haystack = "ssad"
needle = "sad"

def solution():
    nedlen = len(needle)
    for p1 in range(0,len(haystack)):
        if haystack[p1] in needle:
            guess = haystack[p1:(nedlen+p1)]
            if guess == needle:
                return p1
    return -1

#did this one by myself. It is not very effiecent as on Leetcode it passed but only beat 10% of imputs. The below solution I also came up with and it uses a while loop and for some reason it now beats 44% of solutions. Weird.

def solution2():
    nedlen=len(needle)
    p1 = 0

    while p1<=len(haystack)-nedlen:
        if haystack[p1]==needle[0]:
            guess = haystack[p1:(nedlen+p1)]

            if guess == needle:
                return p1
        p1+=1
print(solution2())
