#here we are going to be given a string 's' which containes words, numbers, or weird characters. The goal here is to figure out if you remove all that is the string a palindrome

s = "ab_a"

def solution():
    #for the brute force approach we are going to loop through the entire word and lowercase and remove all non english characters/spaces. Once that is done we will then inverse the word and see if it == the normal word. If so we return palindrome

    #we can use the built in re function to strip all crazy characters
    import re

    #remove all weird characters and remove spaces
    low = s.lower()
    lows = re.compile('\W')
    sstring = re.sub(lows,'',low)
    for char in sstring:
        if char == '_':
            sstring = sstring.replace('_','')

    #now we simply need to see if the word is the same backwards and forwards
    backw = []
    forw = list(sstring)
    for char in forw[::-1]:
        backw.append(char)

    if forw==backw:
        return True
    else:
        return False

#let's try to run two pointer and add to two diffrent arrays

def solution2():
    i, j = 0, len(s) - 1

    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1

    return True

print(solution())
