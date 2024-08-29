#here we are going to be given an array of arrays. These arrays will form a geometric object and you will have to return the perimiter of the object moving inwards.
#an example of this is the array [[1,2,3],[4,5,6],[7,8,9]]. Row one of the array is 123, second row is 456, and third row is 789. So the answer would be [1,2,3,6,9,8,7,4,5].

#below is teh example.
matrix = [[1,2,3],[4,5,6],[7,8,9]]

#constraints
# I think there will always be a uniform subarray given so 3x3's or 4x4's. The array will have no negative numbers. There will always be an answer. The numbers are whole.

#brute force
#i think the proper way to go about this would be to find the assumptions. The first subarray will always be the top, last will always be the last. The trick is to figure out the skip. As we count we can eliminate them from array.

def solution():
    result = []
    left,right=0,len(matrix[0])
    top,bottom=0,len(matrix)
    #above created the pointers on each corner. The idea is that we loop through and squeeze the geometry.

    #now we create the while loop with for loops inside.
    while left<right and top<bottom:
        #get every i in top row
        for p1 in range(left,right):
            result.append(matrix[top][p1])
        top +=1
        for i in range(top,bottom):
            result.append(matrix[i][right-1])
        right -= 1
        if not (left<right and top<bottom):
            break
        for i in range(right-1,left-1,-1):
            result.append(matrix[bottom-1][i])
        bottom-=1
        for i in range(bottom-1,top-1,-1):
            result.append(matrix[i][left])
        left+=1
    return result
print(solution())