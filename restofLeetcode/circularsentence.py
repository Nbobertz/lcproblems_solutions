#here we are going to be given a string consisting of characters and spaces. The idea is we need to see if the string is circular; True or False

#a string is circular if the last character of the first word is equvilent to the first character of the second word and vice versa. The last character of the last word must == the first character of the first word.

sentence = "leetcode exercises sound delightful"

def solution():
    spl = sentence.split(' ')
    for p1 in range(0,len(spl)):
        curr = spl[p1]
        if p1==len(spl)-1:
            nxt = spl[0]
        else:
            nxt = spl[p1+1]
        if curr[-1]!=nxt[0]:
            return False
    return True


print(solution())