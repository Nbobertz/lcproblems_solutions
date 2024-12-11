#here we are going to be given a string and it is our goal to see if it is a palindrome; that it can be read backwareds and forwards and be the same
import string

s = s = "Was it a car or a cat I saw?"

def solution():
    t = s.translate(None,string.punctuation)
    arr1 = []
    arr2 = []

    counter = 0
    for p1 in range(0, len(t)):
        counter -= 1
        tmp1 = t[p1]
        tmp2 = t[counter]
        if tmp1.lower() != tmp2.lower():
            return False
    return True

def solution2():
    l, r = 0, len(s) - 1

    while l <= len(s) or r >= 0:
        char1 = s[l]
        char2 = s[r]

        if char1.isalpha() == False:
            l += 1
            if l>len(s)-1:
                return False
            char1 = s[l]
        if char2.isalpha() == False:
            r -= 1
            char2 = s[r]
        if char1.lower() != char2.lower():
            return False
        l += 1
        r -= 1
        if l==len(s)-1:
            return True
    return True

def solution3():
    newStr = ''
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]
print(solution2())