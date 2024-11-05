#here we are going to be given a string of 0's and 1's. Our goal is to determine how many characters we will change to make the integer beautiful. A string is beautiful if you can partition into 1's and 0's of even length.

s= "11000111"

def solution():
    # checking two consecutive characters and change to the first
    # use sliding window to change

    l, r = 0, 1
    answer = 0

    while r < len(s):
        if s[l] != s[r]:
            answer += 1
        l += 2
        r += 2
    return answer


print(solution())