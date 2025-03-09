#here we are given an array and an integer k. The idea is that k elemetns that switch between 0 and 1 is considered a group. The idea is that you need to go though and see how many groups there are.

colors = [0,1,0,0,1,0,1]
k = 6

def solution():
    colors.extend(colors[:(k - 1)])
    count = 0
    left = 0

    for right in range(len(colors)):
        if right > 0 and colors[right] == colors[right - 1]:
            left = right
        if right - left + 1 >= k:
            count += 1

    return count