#we are going to be given two strings (s) and (t) the goal here is to find out if both strings can be used to make an anagram. For example, s would consist of dog and t would be god. Is this an anagram? Yes, so we return True. Rat and car are not so we return False.

#constraints
#so for this we would need to return True or False only.
#Each letter is used only once.

#talk it out
#so for this I think breaking apart the word into an array of characters is the way to go. After this the array will be looped through to figure out if it is in the second word. If the character is then we pop it from the array. If the array len is 0 or empty then we have an anagram. If at any point the character is not in the word then we return False as the letter is not used.

#code it up
s = 'ac'
t = 'ab'

def solution():
    arr1 = list(s)
    oparr= list(t)
    if len(arr1)!=len(oparr):
        answer = False
        return answer
    while len(arr1)!=0 and len(oparr)!=0:
        for char in arr1:
            if char in oparr:
                arr1.remove(char)
                oparr.remove(char)
            elif len(arr1)==0 and len(oparr)==0:
                answer = True
                return answer
            else:
                answer = False
                return answer
    if len(arr1)==0 and len(oparr)==0:
        answer = True
        return answer
    else:
        answer = False
        return answer

answer = solution()
print(answer)
