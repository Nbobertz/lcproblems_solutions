#this is Leetcode 3330. You are given a string; word. And you need to count each occurance of a doubled up letter.

"""Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

You are given a string word, which represents the final output displayed on Alice's screen.

Return the total number of possible original strings that Alice might have intended to type.

Example 1:

Input: word = "abbcccc"

Output: 5

Explanation:

The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", and "abcccc".
"""


word = "abbcccc"
def solution(word):
    output = 1
    for p1 in range(0, len(word) - 1):
        char = word[p1]
        if word[p1 + 1] == char:
            output += 1
    return output

print(solution(word))