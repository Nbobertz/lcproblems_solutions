#here we are going to be given an array of daily temperatures. THe idea here is that we will have to create an array of days we need to wait at each index to get a warmer temperature.

temperatures = [73,74,75,71,69,72,76,73]

def mysol():
    # this is a stack problem, no need to keep track of max.
    answer = []
    t = temperatures

    for p1 in range(len(t)):
        counter = 0
        for p2 in range(p1 + 1, len(t)):
            counter += 1
            if t[p2] > t[p1]:
                answer.append(counter)
                break
            elif p2 == len(t) - 1:
                answer.append(0)
        if p1 == len(t) - 1:
            answer.append(0)
    return answer


def neetcode():
    res = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            # print(stackT,stackInd)
            res[stackInd] = (i - stackInd)
        stack.append([t, i])
    return res

print(neetcode())