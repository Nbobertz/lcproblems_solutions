def solution():
    # we are looking for constraints on a what is called a beautiful index

    # i can only be s-a in length
    # j is another index is the same for b
    # i and j are the starting index points for the word (a or b)

    # a beautiful index is the absolute value of j-i so that that value is <= to k

    # const variables
    a_array = []
    b_array = []
    answer = []

    # capture starting of a
    for i in range(0, len(s) - 1):
        if s[i:i + len(a)] == a:
            a_array.append(i)

    # capture starting of b
    for j in range(0, len(s) - 1):
        if s[j:j + len(b)] == b:
            b_array.append(j)

    # now we have captured both starting points. Now we determine if it's beautiful
    for i in a_array:
        for j in b_array:
            if abs(j - i) <= k:
                answer.append(i)
                break

    # now we sort
    answer.sort()
    return answer