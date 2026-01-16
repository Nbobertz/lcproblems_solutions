#here you are going to be given two arrays with subarray's of ranges. The idea here is that you need to output a list of where the ranges overlap. If you end on an individual point that overlaps just return that point ex. [5,5]

#input
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

def solution():
    # const answer array
    answer = []
    # create two pointers for both lists
    i = j = 0

    # while both lists have unproccessed intervals
    while i < len(firstList) and j < len(secondList):
        start = max(firstList[i][0], secondList[j][0])
        end = min(firstList[i][1], secondList[j][1])

        # logic to count interval
        if start <= end:
            answer.append([start, end])

        # increase pointer
        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1
    return answer

print(solution())