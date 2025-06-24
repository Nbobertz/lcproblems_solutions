
def solution(nums):
    hm = {}

    # Count frequencies
    for num in nums:
        if num not in hm:
            hm[num] = 1
        else:
            hm[num] += 1

    # Convert the hashmap into a list of (key, frequency) tuples and sort by frequency
    sorted_items = sorted(hm.items(), key=lambda x: x[1], reverse=True)

    # Get the top k keys
    arr = []
    for i in range(k):
        arr.append(sorted_items[i][0])

    return arr