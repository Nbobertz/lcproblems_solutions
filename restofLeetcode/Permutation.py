#here we are going to be given two strigns. First, is a shorter string and the second is a longer string. The idea here is that we want to see if a permutaiton of the shorter string exists within the longer string.

s1 = "abc"
s2 = "lecabee"

#the best solution here is to use sliding window to see if we have a permutation. So here we will loop through s2 until we hit a number in s1. If we do then we step into the next letter of s2. if that number exists then we pop from s1 and continue to go.

def solution():
    for p1 in range(0,len(s2)):
        if s2[p1] in s1:
            l,r = 0,1
            while r < len(s1):
                if s2[p1] in s1:
                    r+=1
                if r == len(s1):
                    return True

#neetcode's solution is to convert both strings to array's then store the index point and character of each 'window.' The window is the len of the smaller string. The idea here is to iterate through all possible windows until you get a matching 26 in total matches which means that all 3 letters matched in the window along with the respective 23 other characters

def solution2():
    if len(s1)> len(s2):
        return False

    s1count,s2count = [0]*26,[0]*26
    for i in range(len(s1)):
        s1count[ord(s1[i])-ord('a')]+=1
        s2count[ord(s2[i])-ord('a')]+=1

    matches = 0
    for i in range(0,26):
        matches+=(1 if s1count[i]==s2count[i] else 0)

    l =0
    for r in range(len(s1),len(s2)):
        if matches == 26: return True

        index = ord(s2[r])-ord('a')
        s2count[index] +=1
        if s1count[index] == s2count[index]:
            matches+=1
        elif s1count[index]+1 == s2count[index]:
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2count[index] -= 1
        if s1count[index] == s2count[index]:
            matches += 1
        elif s1count[index] - 1 == s2count[index]:
            matches -= 1
        l+=1
    return matches==26


print(solution2())