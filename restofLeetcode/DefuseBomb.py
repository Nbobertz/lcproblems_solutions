#here we are given an array and k where we have to sum all k numbers to the right or left. + is right, - is left, and 0 replaces all numbers

code = [2,4,9,3]
k= -2

def solution():
    # here we are given an input array and the integer k. If the integer is positive then we simply add that many numbers at the index point ahead. Array wraps around. if the integer is negative we add the negative numbers. Array wraps around. If the k == 0 then all integers =0
    answer = []

    # capture 0 case
    if k == 0:
        for x in range(0, len(code)):
            answer.append(0)
        return answer

    # this is for +
    if k > 0:
        for p1 in range(0, len(code)):
            ssum = 0
            kcount = k
            r = p1 + 1
            while kcount > 0:
                while r < len(code) and kcount>0:
                    ssum += code[r]
                    kcount -= 1
                    r+=1
                r = 0
            answer.append(ssum)
        return answer

    #this is for the -
    if k<0:
        for p1 in range(0,len(code)):
            ssum = 0
            kcount = k*-1
            if p1==0:
                l=-1
            else:
                l=p1-1
            while kcount>0:
                print('here')
                while l>(len(code)*-1) and kcount>0:
                    ssum-=code[l]
                    kcount-=1
                    l-=1
                l=-1
            answer.append(ssum*-1)
        return answer

print(solution())