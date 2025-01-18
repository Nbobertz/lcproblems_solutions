#here we have a problem where the idea is that we have two strings. The first string s is longer then the other two. The other two strings; a and b are also provided along with an integers k.

# The goal here is to return a beautiful index. A beaufiul index is one where the following constraints are met. The index itself is less then the length of s minus (-) the length of a. This index must also be nth index plus the length of a -1 == a. The same goes for b.

def solution():
    # create two arrays to store the results of the a and b strings
    a_array = []
    b_array = []

    # create answer array
    answer = []

    # go through s string and see if there exists any instances of a string in it. If so caputure the index into a-array

    # for i in the range of len of s minus the len of a +1. This is to capture all possible indexes and then see if the word is there
    for i in range(len(s) - len(a) + 1):
        if s[i:i + len(a)] == a:
            a_array.append(i)

    # do the same for b
    for j in range(len(s) - len(b) + 1):
        if s[j:j + len(b)] == b:
            b_array.append(j)

    # now we have all possible start index's for both strings in the s array.
    for i in a_array:  # capture this position
        for j in b_array:
            if abs(j - i) <= k:
                answer.append(i)
                break

    # now we need to sort to satisfy end constraints
    answer.sort()

    # return answer
    return answer