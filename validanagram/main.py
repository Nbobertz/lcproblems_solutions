#here we are going to be given two stirngs of random characters. We need to write an alagorithm that will deterimne if the provided strings are an anagram. Return True if both strings are anagrams. Return false if both strings are not.

#an anagram is a word that uses all other characters from another word. God and Dog is a prime example.

#below is the example anagram. Should return True, the second example should return false:
s = "anagram"
t = "nagaram"

s1 = 'rat'
t1 = 'car'

#I think the best solution here is to turn each string into an array. From there you can loop through both arrays and pop off each character if they exist in both. Should both array's be emply at the end you have an anagram because all elements were removed from both lists.

def solution():
    #turn both stings into array's
    arr1= list(s)
    arr2= list(t)

    #set answer to default False. Now we have to prove that the proivded strings are anagrams.
    answer = False

    #put some conditionals to automatically return false
    if len(arr1)!=len(arr2):
        answer = False
        return answer
    while len(arr1) != 0 and len(arr2) != 0:
        for char in arr1:
            if char in arr2:
                arr1.remove(char)
                arr2.remove(char)
            elif len(arr1) == 0 and len(arr2) == 0:
                answer = True
                return answer
            else:
                answer = False
                return answer
    if len(arr1) == 0 and len(arr2) == 0:
        answer = True
        return answer
    else:
        answer = False
        return answer


print(solution())