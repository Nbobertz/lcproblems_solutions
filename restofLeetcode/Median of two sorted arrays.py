#here we are going to be given two array's of integers (nums1,nums2). Each array is sorted in ascendng order. You have to return the median value of both arrays as if they were each sorted in ascending order.

#the idea here is that you will have to add both array's into one and then run binary serach off it. I think you can use the python sort funciton after appending all data to one array. After this we can then run binary search and finally return the median of the number.

#some things that will catch you. this has to run in o(log(m+1)) time. If the array is even (meaning the middle won't be an integer) you are to take the middle point between those integers; 2 and 3 = 2.5.

nums1 = [0,2]
nums2 = [5,5]

def solution():

    #first we add both array's together
    arrfin = nums1+nums2

    #now we sort
    arrfin.sort()

    #now we see if number is odd or not. This is to help us with the edge case later where we have to return the median of two numbers
    odd = True
    if len(arrfin)%2==0:
        odd = False

    #for odd we don't have to run binary. We can just take the middle of the array and return it
    if odd == True:
        middle = int(len(arrfin)/2)
        answer = arrfin[middle]
        return answer

    #however if odd == False then we simply call middle, do inside and outside ints and then divide them to get float
    if odd ==False:

        #call middle point then do an inside and outside
        middle = int(len(arrfin)/2)
        inside = middle-1
        outside = middle+1

        #now we assign integers in arrfin and return median
        insidele =arrfin[inside]
        outsidele=arrfin[outside-1]
        answer = float((insidele+outsidele)/2)
        return answer





# I did the easy solution to this problem. Simply push the two arrays together and sort. Did not find the most optimal solution but it worked. Below is the neetcode approach.