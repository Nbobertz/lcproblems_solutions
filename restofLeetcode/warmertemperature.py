#here you are given an array of itengers. Each integer represents the average temperature for a day. The goal is to find out how many days you have to wait after each integer point until you have warmer day. For example the array 1,2,3,0,1 would be the answer 1,1,2,1,0.

#the brute force solution here is to use two pointer but you can also use a stack. For the two pointer you simply move hte window for each number. However, this can prove to be very bad efficency as you would have to iterate through ever number in the array as you move left to right. The stack solution is much better as we can simply create a stack and then only add to it if the number at the top is larger. If it is then caputure how long it took to overwirte and throw that into an answer array.

#below is example
temperatures = [55,38,53,81,61,93,97,32,43,78]
#my solution did not work
def solution():
    answer=[]
    p1=0
    stack=[]
    days =0
    while p1<len(temperatures):
        stack.append(temperatures[p1])
        for p2 in range(p1+1,len(temperatures)):
            #print('{a}:{b}'.format(a=temperatures[p1],b=temperatures[p2]))
            if temperatures[p2]<stack[-1]:
                days+=1
            if temperatures[p2]==stack[-1]:
                days+=1
            if temperatures[p2]>stack[-1]:
                answer.append(days+1)
                days = 0
                break
            if p2==len(temperatures) and temperatures[p1]>temperatures[-1]:
                print('{a}'.format(a=temperatures[p2]))
                days=0
                answer.append(days)
        p1+=1
    if len(answer)<len(temperatures):
        loopcycle = len(temperatures)-len(answer)
        for x in range(0,loopcycle):
            answer.append(0)

    return answer

def solution2():
    res = [0]*len(temperatures)
    stack = []

    for i,t in enumerate(temperatures):
        while stack and t>stack[-1][0]:
            stackT,stackInd = stack.pop()
            res[stackInd]=(i-stackInd)
        stack.append([t,i])
    return res


test = solution2()
print(test)
