#given an integer of x, return true if x is a palindrome, otherwise return false. This is a pretty common problem that is ranked easy

#establish constraints
#can the number be a negative number? Answer: Yes the number can be negative. Will all numbers be from the arabic numerical system (1,2,3,ex). Answer: Yes, they are all ABN.

#walk through the solution.
#This is going to be a two pointer algorithm. The easist way to do this would be to take the integer and break it up into an array. For example, let's say we get 1221 for an integer. Here wwe would make an array of [1,2,2,1]. This will allow us to then establish pointer 1 at array[0] which should be 1 and then establish the next pointer at array[01] which should be also 1. From there we will loop through the array and move each pointer in towards the center, if all integers are the same by the time the pointers meet then we have a palindrome

#or we can do the easeir way of just creating a new arraay and taking the -1 position from the first array and adding it into the second array. If both arrays are == then we have a palindrom. Let's try this approach.

#code up the enviroment setup.This is just for local IDE tests.
import random,time
def setup():
    target = random.randint(0,1000)
    print("The target is {a}. Ready, let's go!".format(a=target))
    for x in range(0,4):
        counter = 4-x
        time.sleep(1)
        print(counter)
        if counter == 1:
            time.sleep(.5)
            print('Time to calculate!!!!\n')
            time.sleep(1)
    return target

#code up the solution. 121 is for testing purposes.
def solution():
    strtar = str(target)
    if strtar[0] == '-':
        answer = False
        print(strtar[0])
        return answer
    else:
        array1=[]
        array2=[]
        counter = 0
        for num in strtar:
            counter +=1
            array1.append(num)
            negnum = counter*-1
            array2.append(strtar[negnum])
        if array1 == array2:
            answer = True
        else:
            answer = False
        return answer
target=setup()
answer = solution()
if answer == False:
    print('The answer is {a} because it is not a palidrome (same when read backwards and forwards)'.format(a=answer))
else:
    print('The answer is {a} because it is a palindrome great job!'.format(a=answer))


#time complexity has me beating 75% of people and memory beating 47% of people