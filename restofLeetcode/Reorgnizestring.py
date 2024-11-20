#here we are given a string and the goal is to determine if you can reorginize it by placing the letters next to each other in a way that no letter is repeating more then once. If you can't do this then you return ''


def solution():
    ans = []
    # Min heap ordered by character counts, so we will use
    # negative values for count
    pq = [(-count, char) for char, count in Counter(s).items()]
    heapify(pq)

    while pq:
        count_first, char_first = heappop(pq)
        if not ans or char_first != ans[-1]:
            ans.append(char_first)
            if count_first + 1 != 0:
                heappush(pq, (count_first + 1, char_first))
        else:
            if not pq: return ''
            count_second, char_second = heappop(pq)
            ans.append(char_second)
            if count_second + 1 != 0:
                heappush(pq, (count_second + 1, char_second))
            heappush(pq, (count_first, char_first))

    return ''.join(ans)