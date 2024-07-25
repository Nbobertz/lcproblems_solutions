#We are going to be given an array of integers, your job is to loop through this array and find the largest number with a matching negative number.

#identify constraints
#Are the numbers whole? Answer: Yes they are. Will there always be an answer? Answer: No, if there is no solution the answer is -1

#how we are going to do this.
#Here the algorithm is going to be two pointer. I think the brute force method is going to be to have p1 at the 0 index point and then have p2 loop through to the end of the list looking for the negative integer. if it finds it then it will store the positive value of this integer to a diffrent array. When the first loop is done we will then loop through the seccond arry to see what number is the largest and that is the answer. If there is no answer I will have to print -1

#build the array to test against, not part of the leetcode question but provides testing ground
import random
def setup():
    #designed to create a random list
    arraylen = random.randint(0,100)
    array1 = []
    for num in range(0,arraylen):
        rannum = random.randint(1,100)
        negorpos = random.randint(0,1)
        if negorpos == 0:
            newnum = rannum *-1
            array1.append(newnum)
        else:
            array1.append(rannum)
    return array1

#code up a solution
def solution():
    answer=[0]
    higharray=[]
    for p1 in range(0,len(array1)):
        for p2 in range(p1+1,len(array1)):
            if array1[p1]>0:
                inversed = 0
                if array1[p2]<0:
                    inversed = array1[p2]*-1
                if array1[p1] == inversed:
                    higharray.append(array1[p1])
            else:
                inversed = 0
                if array1[p2]>0:
                    inversed = array1[p2]*-1
                if array1[p1]==inversed:
                    higharray.append(array1[p2])
    for num in higharray:
        if num > answer[0]:
            answer[0]=num
    if answer[0] == 0:
        answer[0]= -1
    return answer[0]


array1=setup()
print(array1)
answer=solution()
print(answer)