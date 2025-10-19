#here we are given an array and have to multiply for everything but itself at the x index.

def solution1():
    answer = []

    for p1 in range(0, len(nums)):
        tmp = 1
        for p2 in range(0, len(nums)):
            if p2 != p1:
                tmp = tmp * nums[p2]

        answer.append(tmp)
    return answer

