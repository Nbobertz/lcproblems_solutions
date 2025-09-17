"""This is an intresting problem as it can be solved many diffrent ways but the best way is to sort via bucket sort where we create an array and at each point we store the numbers at that point"""


nums = [1,2]
k = 1
def solution():
    # build hashmap
    hm = {}
    for n in nums:
        if n not in hm:
            hm[n] = 1
        elif n in hm:
            hm[n] += 1

    # build the bucket sort list
    bucket = []
    for space in range(len(nums) + 1):
        bucket.append([])

    for num, freq in hm.items():
        bucket[freq].append(num)

    # append from the back to get the k most frequent elements
    answer = []
    for x in bucket[::-1]:
        for num in x:
            answer.append(num)
        if len(answer) == k:
            return answer