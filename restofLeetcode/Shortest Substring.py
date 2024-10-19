#the idea here is that we are going to be given two strings. s and t. We are to take s and figure out if any of the characters in t are in it. If they are we are to return the shortest substring that contains them.

#if no substring exists we are to return "" showing nothing

# this can be done with either a sliding window solution or a double/tripple hashmap. Maybe we can do this with just an array and pop.

s = "OUZODYXAZV"
t = "XYZ"

def solution():
    occurance ={}
    posindex = {}
    lengthot = len(t)


    for p1 in range(0,len(s)):
        if s[p1] in t and s[p1] not in occurance:
            occurance.update({s[p1]:1})
            posindex.update({s[p1]:[p1]})
#my solution did not work as it could not identify when the strings change. Here is neetcodes

def solution2():
    if t == "":
        return ""

    countT, window = {}, {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in countT and window[c] == countT[c]:
            have += 1

        while have == need:
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = r - l + 1

            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l: r + 1] if resLen != float("infinity") else ""


print(solution2())