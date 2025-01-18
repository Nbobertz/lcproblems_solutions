#here we are given two stings and the idea is to merge alternative placements until you hit the max of one stirng. If you hit he max then go ahead and append the remainder of the other.

word1 = "abc"
word2 = "pgrsd"
def solution():
    output = []  # used to store the characters
    l = min(len(word1), len(word2))

    for i in range(l):
        output.append(word1[i])
        output.append(word2[i])

    # append the remaining to the output array
    output.append(word1[l:])
    output.append(word2[l:])

    return "".join(output)