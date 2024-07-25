#if the array cointains duplicate itegers return False else return True

nums = [1,5,-2,-4,0]

def solution():
    array1 = []
    counter2 = 0
    counter1=0
    while (len(nums)+counter2)!=counter1:
        counter2+=-1
        p1=nums[counter1]
        p2=nums[counter2]
        if len(nums)==1:
            answer = False
            return answer
        if p1 == p2:
            answer =True
            print('here2')
            return answer
        if p1 in array1 or p2 in array1:
            answer = True
            print('here')
            return answer
        else:
            array1.append(p1)
            array1.append(p2)
        print(array1)
        counter1+=1
    if (len(nums)+counter2)==counter1:
        answer=False
        return answer

answer = solution()
print(answer)