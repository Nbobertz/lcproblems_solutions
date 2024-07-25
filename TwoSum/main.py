import random,time

#given an array of integers, return the indices of the two numbers that add up to a given target

#step 1: verify constraints: Ask questions to understand question better. Figure out edge cases
#are all of numbers positive or can they be negative? Answer: All numbers are positive
#are there duplicate numbers? answer: there are no duplicates
#will there always be a solution available? answer: no there might not always be a solution
#what do we return if there is no solution? answer: Just return null
#can there be multiple pairs that add up to a target? answer: no only 1 pair at a time

#step 2: write out test cases. First, best test case
#target = 11
#array1 = [1,3,7,9,2]
#answer return = [3,4]
#
#target = 25
#array 1 = [1,3,7,9,2]
#answer return = null
#
#target = 5
#array1 = [1,3,7,9,2]
#answer return = null

#step 3: without code and talking through it
#I guess the best case scenario would be to brute force it. Add up every possible pair of numbers and then see if I can get to the number. This is two pointer algorithm. So we would construct an array, get our target number, then create p1 at the 0 point of the array and p2 at the 1 point of the array. From here we would have our target for p2 be (target-p1). So if our target number is 25 and our first number in the array(p1) is 5 our target for array[1-end] would be 20.

#step 3: code up the brute force

#creates a random array filled with numbers
def setup():
    #creates the random length of array
    rand_list_len = random.randint(5,15)

    #creates the array
    array2=[]
    for pos in range(0,rand_list_len):
        #creates random number
        num1 = random.randint(0,20)
        array2.append(num1)
    array1 = sorted(array2)
    time.sleep(1)
    print('Here is the array of random length with random numbers')
    print(array1)
    time.sleep(1)

    #creates random target
    num2 = random.randint(0,20)
    target=num2
    print('The random target for the index position to hit is {a}'.format(a=target))
    time.sleep(1)
    return target,array1
def twosum():
    answer = []
    for p1 in range(0,len(array1)):
        for p2 in range(p1+1,len(array1)):
            if array1[p1]+array1[p2] == target:
                answer.append(p1)
                answer.append(p2)
                return answer
                exit

print('This is the brute force two pointer method with TC of O(n^2)\n')
target,array1 = setup()
answer = twosum()
if answer == None:
    print('There is no answer/Null')
else:
    print('\nThe index position to hit for the assigned values to add up to {a} is {b} and {c} ({d})'.format(a=target,b=answer[0],c=answer[1],d=answer))
    print(answer)