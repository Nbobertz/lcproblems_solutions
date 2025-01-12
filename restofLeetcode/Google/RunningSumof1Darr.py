#here we are getting the running sum and returning it an an answer arry.

nums = [1,2,3,4]

def solution():
    answer = []

    # loop through array, if integer is first just append. If not then sum and append to answer
    for p1 in range(len(nums)):
        if p1 == 0:
            answer.append(nums[p1])
        else:
            tmpsum = answer[-1] + nums[p1]
            answer.append(tmpsum)
    return answer