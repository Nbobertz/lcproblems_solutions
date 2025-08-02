#Here we are given an array of integers in ascending order. The idea is that we will have to return an array where a provided target inter is hit and the array itself has to be the index of the integers.
#Also you can only use constant space so no hashmap.


numbers = [1,2,3,4,5]
target = 7

def hash_solution():
    # think I can do a hashmap pass
    hm = {}
    for i, n in enumerate(numbers):
        rem = target - n
        if rem in hm:
            if hm[rem] < i:
                return [hm[rem] + 1, i + 1]
        hm[n] = i

def solution():
    # this is done with a two pointer pass. Since the array is already ascending then all we have to do is walk backwards with a r pointer and forwards with a l pointer

    l, r = 0, len(numbers) - 1

    while l < r:
        ln = numbers[l]
        rn = numbers[r]
        # logic to check
        if ln + rn > target:
            # to the right of the target
            r -= 1
        elif ln + rn < target:
            # to the left of the target
            l += 1
        elif ln + rn == target:
            return [l + 1, r + 1]