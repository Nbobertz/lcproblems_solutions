#here we are going to be given an array of integers. The array length and the maximum value of the integer is given. It is your job to loop through the array and find the missing number

#I think the best solution here is to first capture the len of the array, assigne that len to a range in a max set(). after that as well loop through the array we will remove from the second array. What is left is the remainder

nums = [0]

def solution():
    #create the empty array and then add all sequential numbers to it from the len of nums. [3,0,1] is 3 so this array will be [1,2,3]
    duparr = []
    for p1 in range(0,len(nums)+1):
        duparr.append(p1)

    #now we loop through nums and remove (not pop as that is index point) from the first array. what's left is the final answer
    for num in nums:
        if num in duparr:
            duparr.remove(num)
    return duparr[0]

print(solution())