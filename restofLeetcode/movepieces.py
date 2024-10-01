#here we are going to be given a string comprising only of L, R, and _ characters. After this we will be given a target string comprising of simliar characters. The idea here is that you can only move a L if there is a _ to the left and a R if there is a _ to the right. Letter's cant overlap each other.


#the trick here is to move characters in a string until the string matches the target string. Two pointer can be used here so long as you capture the pointer elements at index.

sstart = "_L__R__R_"
target = "L______RR"

def solution():
    start = list(sstart)
    tar = list(target)
    answer = False
    if len(start)!=len(target):
        return answer
    if len(start)==2 and start[-1]=='R':
        answer = False
        return answer
    if len(start)==2 and start[0]=='L':
        answer = False
        return answer
    l,r = 0,len(start)-1
    tmp = start

    while l<=r:
        #print(l)
        #print(r)
        if tmp[l]=='L' and tmp[l-1]=='_':
            while tmp[l-1]=='_':
                #print('here_l')
                tmp[l] = '_'
                tmp[l - 1] = 'L'
                if tmp == tar:
                    answer = True
                    return answer
                l -= 1
                #print(tmp)
                if l == 0:
                    #print('here_l2')
                    break
        if tmp[r]=='R' and tmp[r+1]=='_':
            while tmp[r+1]=='_':
                #print('here')
                tmp[r]='_'
                tmp[r+1]='R'
                if tmp==tar:
                    answer=True
                    return answer
                r+=1
                #print(tmp)
                if r+1>=len(tmp):
                    #print('here2')
                    break
        l+=1
        r-=1
    return answer
help = solution()


#did not end up getting it
print(help)