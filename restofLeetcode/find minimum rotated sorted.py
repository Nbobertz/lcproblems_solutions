#here we are going to be given an array of random length with integers in it. This array will be presorted in ascending order and then rotated to the right n times. The goal here is to return the minimum integer in the array in O(log n) time. Each inteer is unique, there will always be a number.

#The easiest way to to do this is to simply run sort on the array and then call the [-1] position. This should return the lowest in the array. However, this might be to easy a 'harder' way to do this is the find the lowest number in the array and then count how many index points to the begining.

#example and solution below
nums = [3,4,5,6,1,2]

def solution():
    numar = nums
    numar.sort()
    answer = min(numar)
    return answer


print(solution())