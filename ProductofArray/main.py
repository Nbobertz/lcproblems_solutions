#here we are going to take a random array and give an output of every single value in that array. This problem has to run in N(o) and also you are not allowed to use the division sign as that would make it to easy

#had to watch neetcode for the solution. The trick here is to first multiply by the left and thne the right. After this multiply by each last value and you have the answer

#below is test case
nums = [1,2,3,4]

def solution():
    res =[1]*(len(nums))

    #for the prefix multiple
    prefix = 1
    for i in range(len(nums)):
        res[i]=prefix
        prefix *=nums[i]
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        res[i]*=postfix
        postfix *= nums[i]

    return res

answer=solution()
print(answer)