#here we are given two strings; the first is the starter string and the second is a new string that adds exactly 1 character. We need to find that character and return it.

s = "abcd"
t = "abcde"

def solution():
    # this can be done with a hashmap in O(n)

    hm = {}  # character:integer of time seen
    # logic to see if we have it more then the other time

    # first loop through s adding all chars to hm and incrementing if there is more then on
    for char in s:
        if char not in hm:
            hm[char] = 1
        elif char in hm:
            hm[char] += 1

    # now loop through and subtract chars from hm. If any is left or we encounter another character not in the hm return that as answer
    for char in t:
        if char in hm:
            hm[char] -= 1
        elif char not in hm:  # catches a new character
            return char

    # check hashmap to see what char has 1 remaining. Since we only add one more character
    for key, value in hm.items():
        if value != 0:
            return key


print(solution())