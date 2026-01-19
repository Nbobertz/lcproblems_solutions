#here we are given an array where each number is a possible move forwards or backwards in the array.
# You start at the 0th index and what happens is that you can either move forwards or backwards based of whatever new index number you fall on.
#if you can reach the target provided you end up returning true because you can find it.
from collections import deque


arr = [4,2,3,0,3,1,2]

start = 5

def solution():
    # This is a dynamic programming problem because I can't use greedy to reach the end. We need to see if we can land on a 0 value index from the starting point.

    n = len(arr)  # capture the length of the arr array
    q = deque()

    # capture base case
    if len(arr) != 0:
        q.append(start)
    else:
        return False

    while q:
        node = q.popleft()

        # see if we reached zero
        if arr[node] == 0:
            return True
        if arr[node] < 0:
            continue

        # check to see next steps
        for i in [node + arr[node], node - arr[node]]:
            if 0 <= i < n:
                q.append(i)

        # mark as visited
        arr[node] = -arr[node]

    return False

print(solution())