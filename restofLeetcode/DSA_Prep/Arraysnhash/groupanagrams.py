def solution():
    answer = []  # answer array to return
    visited = [False] * len(strs)  # to see what has been grouped

    for p1 in range(len(strs)):
        # check to see if visited
        if visited[p1]:
            continue

        hm = {}
        for char in strs[p1]:
            if char not in hm:
                hm[char] = 1
            elif char in hm:
                hm[char] += 1

        sub_arr = [strs[p1]]  # create subarray and add p1 to it
        visited[p1] = True  # mark p1 as visited

        # now loop through p1+1->len(strs)
        for p2 in range(p1 + 1, len(strs)):
            hm2 = hm.copy()
            if visited[p2]:  # skip if we have seen this one
                continue

            # see if anagram to p1
            for char in strs[p2]:
                if char not in hm2:
                    break
                elif char in hm2:
                    hm2[char] -= 1
                    if hm2[char] == 0:
                        hm2.pop(char)

            # see if hm2 has stuff in it
            else:
                if len(hm2) == 0:
                    sub_arr.append(strs[p2])
                    visited[p2] = True  # add to visited set

        answer.append(sub_arr)
    return answer