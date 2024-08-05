#here we are going to take a random array and give an output of every single value in that array. This problem has to run in N(o) and also you are not allowed to use the division sign as that would make it to easy

#had to watch neetcode for the solution. The trick here is to first multiply by the left and thne the right. After this multiply by each last value and you have the answer

#below is neetcode answre

#below is test case
nums = [2,3,5,0]

# def solution():
#     res =[1]*(len(nums))
#
#     #for the prefix multiple
#     prefix = 1
#     for i in range(len(nums)):
#         res[i]=prefix
#         prefix *=nums[i]
#     postfix = 1
#     for i in range(len(nums)-1,-1,-1):
#         res[i]*=postfix
#         postfix *= nums[i]
#
#     return res

def solution2():
    #here we are going to compute the pre and post fix for the above
    answer = []
    print(nums)

    #below is going to the be prefix
    prefix=[]
    prefixnum=0
    for p1 in range(0,len(nums)):
        if p1 == 0:
            prefixnum=1
            prefix.append(nums[p1]*prefixnum)
        else:
            prefix.append(nums[p1]*prefix[p1-1])
    print(prefix)

    #now we are going to do postfix
    postfix = []
    postfixnum = 0
    counter = 0
    for p1 in range(0,len(nums)):
        counter+=-1
        if counter == -1:
            postfixnum = 1
            postfix.insert(0,nums[counter]*postfixnum)
        else:
            postfix.insert(0,nums[counter]*postfix[counter+1])
    print(postfix)
    #now we are going to multiply the nums index by the pre and postfix and then insert it into our final product

    for p1 in range(0,len(nums)):
        finalnum = 0
        prestore=0
        poststore=0
        if p1 == 0:
            prestore=1
            poststore=postfix[p1+1]
            finalnum =prestore*poststore
            answer.append(finalnum)
        elif p1 == len(nums)-1:
            poststore = 1
            prestore=prefix[p1-1]
            finalnum = prestore*poststore
            answer.append(finalnum)
        else:
            poststore=postfix[p1+1]
            prestore=prefix[p1-1]
            finalnum = prestore*poststore
            answer.append(finalnum)
    return answer

answer=solution2()
print(answer)