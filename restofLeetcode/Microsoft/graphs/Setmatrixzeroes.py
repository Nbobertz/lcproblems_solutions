#here we are going to find a 0 in a matrix and then set all integers in it's row and collumn to zero.

#simply keep track of the rows and cols as you iterate through, if you find a zero add the row and col to a set. From here simply loop back over and change everythning.

matrix = [[1,1,1],[1,0,1],[1,1,1]]

def solution():
    R = len(matrix)
    C = len(matrix[0])
    rows, cols = set(), set()

    # Essentially, we mark the rows and columns that are to be made zero
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # Iterate over the array once again and using the rows and cols sets, update the elements
    for i in range(R):
        for j in range(C):
            if i in rows or j in cols:
                matrix[i][j] = 0