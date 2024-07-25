#the point here is to be given an array of random numbers and have a program that can loop through it and find three consecutive odd numbers. Return the numbers in an array

#here we setup the random array
import random,time
def setup():
    arrlen = random.randint(0,30)
    arr = []
    for num in range(0,arrlen):
        arr.append(random.randint(1,100))
    return arr


#constraints= no negative numbers, array does not loop when hitting the end, 1 counts as an odd number for this scenario.
#build the logic. Here I would build 3 pointers and just see if the next two numbers are odd if pointer 1 lands on an odd number
#build the code
def solution():
    answer = []
    if len(arr) >= 3:
        for p1 in range(0, len(arr)):
            if p1 == len(arr) - 2:
                answer = 'There are no consecutive 3 odds'
                return answer
            if arr[p1] % 2 != 0:
                p2 = p1 + 1
                p3 = p2 + 1
                if arr[p2] % 2 != 0 and arr[p3] % 2 != 0:
                    answer.append(arr[p1])
                    answer.append(arr[p2])
                    answer.append(arr[p3])
                    return answer
    return answer


#call everthing and make sure it works
arr=setup()
print('Below is the array to loop through to find 3 consecutive odds')
print(arr)
answer=solution()
print(answer)