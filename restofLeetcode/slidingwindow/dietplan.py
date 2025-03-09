#here we are given an integer array and an integer. The integer is the number of days (indexes) that we can go to score points. The idea here is that we can loop through the array and return the pionts we have scored over the diet.

calories = [1,2,3,4,5]
k = 1
lower = 3
upper = 3

#leetcode 1176

def solution():
    s = sum(calories[:k])

    points = 0

    if s < lower:
        points -= 1
    elif s > upper:
        points = 1

    for i in range(k, len(calories)):
        s += -calories[i - k] + calories[i]
        if s < lower:
            points -= 1
        elif s > upper:
            points += 1

    return points