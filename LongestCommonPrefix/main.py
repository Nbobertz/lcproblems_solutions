#you are going to be given an array of strings. Your goal is to write a program that can easily find the longest prefix from amoung them. ex. flower, flow, and flight would be 'fl'

#I think the best way to go about this is to find the shortest string in the given strings. From there we will loop through that string and then add one pointer for each common prefix until you get the max.

#example
strs = ['ab','a']


def solution():
    strs2=strs

    #grab the shortest of the strings as the base
    shrtstr=len(strs2[0])
    shrt=strs2[0]
    for p1 in range(0,len(strs2)-1):
        strlen = len(strs2[p1])
        if strlen<shrtstr:
            #shrt is the shortest string
            shrt=strs2[p1]
            print(shrt)
            #popped out the string so it does not flag itself
            strs2.pop(p1)

    #now we are going to for loop through the array while keeping track.
    #we inilize answer, take a p1 in for loop of the shortest string, and then loop through each individual string in order.
    answer = ''
    for p1 in range(len(shrt)):
        for string in strs2:
            if string[p1]!= shrt[p1]:
                return answer
        answer += shrt[p1]
    return answer

def solution2():
    res = ''
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i]!=strs[0][i]:
                return res
        res+=strs[0][i]
    return res




print(solution2())
