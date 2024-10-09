#here we are going to be given a 2d matrix that consists of a set of rows with integers in them. Each one of these rows is sorted in non-decreasing order. These rows are ordered so that the last integer in the row is less then the descending/next row.

#your goal here is to determine if a provided target number is in the array. You need to do this in o(long(m*n))time

#I think the easiest way to do this is to use the binary search algorithm. We will be given an set amount of arrays'. From here we will take the last point of each subarry. If our target falls inbetween these points we then do two pointer to see if it's in the subarray; think of this as a nested binary search array problem.

#matrix = [[1,3,5,7],[10,11,16,20]]
#target = 3
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]

target = 16

def solution():
    for p1 in range(0,len(matrix)):
        #first we are going to see if we can isolate the 'row'
        if p1==len(matrix)-1:
            #catches if for whatever reason the target is more then the [-1] point in the last subarray. Returns false
            if target>matrix[p1][-1]:
                answer = False
                return answer
            else:

                #first we convert to set to get rid of duplicates, then back to list, then sort to put back in order.
                arr1 = set(matrix[p1])
                arr = list(arr1)
                arr.sort()
                l,r = 0,len(arr)-1
                while l<=r:
                    diff = int((l+r)/2)
                    if target<arr[diff]:
                        r = diff-1
                    if target>arr[diff]:
                        l = diff+1
                    if target==arr[diff]:
                        answer = True
                        return answer
            answer = False
            return answer

        #now we do all the subarrays up to the last subarray. Since we know last sub position we can just point ahead with p1+1
        if target==matrix[p1][0] or target==matrix[p1+1][0]:
            answer = True
            return answer
        if target>matrix[p1][0] and target<matrix[p1+1][0]:

            #we convert to set and back to list to get rid of any duplicates, then we sort
            arr=set(matrix[p1])
            arr1=list(arr)
            arr1.sort()

            #below catches if only one number exists in p1 subarray
            if len(arr1)==1 and target!=arr1[0]:
                answer = False
                return answer

            #below is binary search
            l,r = 0,len(arr1)-1
            while l<=r:
                diff = int((l+r)/2)
                print(diff)
                print(arr1)
                print(arr1[diff])
                if target<arr1[diff]:
                    r=diff-1
                if target>arr1[diff]:
                    l=diff+1
                if target==arr1[diff]:
                    answer = True
                    return answer
    answer = False
    return answer




print(solution())