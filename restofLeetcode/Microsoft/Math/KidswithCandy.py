#here you are given a bunch of kids with candy represented in an array. You also have a bag of extra candy.
#You can only hand out x amount of extra candy to each kid.
#return a bool array of if the ith kid is now the largest kid with candy

candies = [2,3,5,1,3]
extraCandies = 3

def solution():
    # bool arr
    answer = []  # store as strings 2nd or bools 1st

    oldcandy = max(candies)

    for x in candies:
        bigcandy = x + extraCandies
        if bigcandy >= oldcandy:
            answer.append(True)
        else:
            answer.append(False)

    return answer