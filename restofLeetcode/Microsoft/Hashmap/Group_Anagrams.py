#Here we are given a series of input strings. We have to loop through these strings and group all anagrams together into an output

strs = ["eat","tea","tan","ate","nat","bat"]

def solution():
    result = {}
    for item in strs:
        itemResult = []
        for letter in item:
            itemResult.append(letter)
        itemResult.sort()
        itemResult = ''.join(itemResult)
        if itemResult in result:
            result[itemResult].append(item)
        else:
            result[itemResult] = [item]
    my_list = [i for i in result.values()]
    return my_list

print(solution())