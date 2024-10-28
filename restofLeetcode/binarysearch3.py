#here we are going to do binary search again. We have an array and a target integer. The array is sorted in ascending order. The idea here is that if the target number is in the array then we return it's index point. The idea is that you have to find this in O(longn) time.

#we are going to mix it up and import a bunch of random integers to make this work. The idea is that we will create a bunch of random stuff.
import random

ranlen = random.randint(0,100)
nums = []
for p1 in range(0,ranlen):
    num = random.randint(0,200)
    nums.append(num)
target = random.randint(0,200)
nums.sort()
#nums = [-1,0,2,4,6,8]
#target = 4

print(nums)
print(target)

def solution():
    l,r = 0,len(nums)-1

    while l<=r:
        half = int((l+r)/2)

        if nums[half]<target:
            l = half+1
        if nums[half]>target:
            r = half-1
        elif nums[half]==target:
            return 'index of {a} is at {b}'.format(a=target,b=half)

    return 'There is no number {a} in the array'.format(a=target)

print(solution())