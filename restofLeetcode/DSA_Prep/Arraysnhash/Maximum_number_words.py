#Here we are given a string and asked to find the maximum number of words you can type without using a charcter in the word.


# Convert to list, then pop words that have the broken letters in it
def soltuion():
    ll = text.split(' ')
    answer = len(ll)
    print(ll)

    for word in ll:
        for char in brokenLetters:
            if char in word:
                answer -= 1
                break

    return answer