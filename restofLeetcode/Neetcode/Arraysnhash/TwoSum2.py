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
