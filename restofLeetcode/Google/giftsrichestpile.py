#here we are given an array and an integer. We must find the maximum number in the array and square it o the floor. After all of this is done we return the sum of the array.

gifts = [56,41,27,71,62,57,67,34,8,71,2,12,52,1,64,43,32,42,9,25,73,29,31]

k = 52

def solution():
    for x in range(0, k):
        mmax = max(gifts)
        tmpnum = int(mmax ** .5)
        for x in range(0, len(gifts)):
            if gifts[x] == mmax:
                gifts[x] = tmpnum

    answer = sum(gifts)
    return answer


print(solution())


#below uses heaps
def solution2():
    gifts = [-v for v in gifts]
    heapify(gifts)
    for _ in range(k):
        heapreplace(gifts, -isqrt(-gifts[0]))
    return -sum(gifts)