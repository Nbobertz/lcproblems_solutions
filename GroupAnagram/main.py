#here you are going to be given an array of multiple strings. You are going to have to loop through this array and determine which strings are an anagram. Once you find an anagram then you will bunch all other similiar anagrams together.

#constraints
#there will always be a string in the array
#The string will only consist of lowercase english letters

#brute force
#the brute force method here might be the most efficent. We are going to loop through the array and each string is going to be added to a hashmap {string:letters} this will allow us to use an in statment. Then for each string we will use for n in string. If we get an array lump those words together. As we loop through the array the word will get added to the answer as a subarray to make lumping them together.



#below is the example array
strs = ["eat","tea","tan","ate","nat","bat"]



#the idea with the below solution is that I will loop through each word and add it to a dictonary. In this dictionary I will then add every letter to the word as a value. From here I will then loop through the rest of the words and see what anagrams I can use.
def solution():
    answer = []
    hmap={}
    for p1 in range(0,len(strs)):
        tmp = list(strs[p1])
        print(tmp)
        hmap.update({strs[p1]:None})
        for p2 in range(0,len(tmp)):
            print(tmp[p2])
            hmap[strs[p1]]+=tmp[p2]
    print(hmap)

solution()