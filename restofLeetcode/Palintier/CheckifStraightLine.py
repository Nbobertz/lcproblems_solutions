#we are given an array and asked to see if it is a straight line.

coordinates = [[0,0],[0,1],[0,-1]]




def solution():
    l = 0

    while l < len(coordinates):
        if coordinates[l] == [0,0]:
            pass
        else:
            # positive check
            if coordinates[l][1] - coordinates[l][0] != 1:
                if coordinates[l][1] - coordinates[l][0] == -1:
                    pass
                else:
                    return False

        l += 1
    return True

def propersolution():
    l = 0

    while l < len(coordinates):
        if coordinates[l] == [0,0]:
            pass
        else:
            # positive check
            if coordinates[l][1] - coordinates[l][0] != 1:
                if coordinates[l][1] - coordinates[l][0] == -1:
                    pass
                else:
                    return False

        l += 1
    return True

print(solution())