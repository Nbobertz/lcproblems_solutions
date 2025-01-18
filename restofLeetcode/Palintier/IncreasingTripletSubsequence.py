#Here the idea is that you are given an array and you need to determin if a subsequence exists of three ascending numbers

def solution():
    first_num = float('inf')
    second_num = float('inf')
    for n in nums:
        if n <= first_num:
            first_num = n
        elif n <= second_num:
            second_num = n
        else:
            return True
    return False