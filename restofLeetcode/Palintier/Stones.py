#the idea here is that we are given an array of integers that represent stone sizes. Every revolution we take two of the largest stones and smash them together. The remainder is then added to the ston lest. Figure out the remainder


stones = [2,7,4,1,8,1]

def solution():
    while len(stones) >1:
        stones.sort()
        cur = stones.pop()-stones.pop()
        if cur:
            stones.append(cur)

    return stones[0] if stones else 0


def heapsolution():
    #here we use a max heap and multiply it all by -1 so that we get the largest on the top. From there we simply need to pop from the top and then do our conditional and then append to the heap

    #multiplpy by -1
    for x in stones:
        stones[i] *= -1

    #heapify stones
    heapq.heapify(stones)

    #while len is greater then 1 take top two and smash together
    while len(stones) > 1:
        stone_1 = heapq.heappop(stones)
        stone_2 = heapq.heappop(stones)

        if stone_1 != stone_2:
            heapq.heappush(stones,stone_1 - stone_2)


    return heapq.heappop(stones) if stones else 0
print(solution())