#here we are going to be given a string of 'words' as a string. You goal is to reverse the string and return it. So the string 'hello my name is Nick' would be 'Nick is name my hello'
import collections

#below is example
s = "  hello world  "

#below is solution had to use the cracking code interview as there was one edge case I could not catch in On
def solution():
    string_builder = collections.deque()

    start = -1
    i=0
    while i<len(s):
        if s[i]!=' ':
            start = i
            while i<len(s) and s[i]!=' ':
                i+=1

            string_builder.appendleft(s[start:i])
            i-=1
        i+=1

    return ' '.join(string_builder)

print(solution())