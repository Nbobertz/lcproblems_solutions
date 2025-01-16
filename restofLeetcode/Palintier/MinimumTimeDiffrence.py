#here we are given a set of strings and asked to find the diffrence between them when they are in time format.

timePoints = ["23:59","00:00"]

def solution():
    # first we time the first integer by 60 by spliting the ingress string
    minutesarray = []
    minimum = 1441
    for x in timePoints:
        tmp = x.split(':')
        tmp_hour = tmp[0]
        minutes = int(tmp_hour) * 60
        finalcount = int(tmp[1]) + minutes
        minutesarray.append(finalcount)

    # sort the array allows us to do one pass
    minutesarray.sort()

    # count the min for each 'time'
    result = 1441
    for i in range(1, len(minutesarray)):
        tmpnum = minutesarray[i] - minutesarray[i - 1]
        result = min(tmpnum, result)

    # handle the circulare case
    return min(result, 1440 + minutesarray[0] - minutesarray[-1])