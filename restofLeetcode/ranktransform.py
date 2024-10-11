#here we are going to be given an array of integers. We will have to output an array where each integer in the first array is given it's index. Ex. [55,22,33,1] would be [4,2,3,1] due to it's size in the array.

#the brute force solution here is to capture the len of the array. Then we know the range of items that we will assign. After that we invert the array and run a hashmap. Finally we loop through the array and assign a new value to a new array dependent on what we have.

#example below
arr = [1,1,1,2,3,4,5,10]

def solution():
    answer = []

    #this constructs list to set then back to list. Get's rid of duplicates
    tmpar = arr
    tmpar = set(tmpar)
    tmpar = list(tmpar)
    tmpar.sort()

    #now we loop through and pull the
    for x in arr:
        tmp = x
        if x in tmpar:
            tmppos = tmpar.index(tmp)
            tmpfin = tmppos+1
            answer.append(tmpfin)
    return answer


print(solution())