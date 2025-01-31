#check to see if it is a linear line across the board.

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

(x0,y0),(x1,y1)=coordinates[:2]

answer = True
for x,y in coordinates:
    if (x1-x0)*(y,y1)!=(x-x1)*(y1-y0):
        answer = False
print(answer)
