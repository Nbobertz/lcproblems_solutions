#the idea here is that you have a phone where each digit corespondes to characters. You are given digits and the idea is that you need to print off all possible digit combinations

digits = "34"

def solution():

    #here we can have a dictionary of integrers and the characters it corespondes with
    pad = {"1":[],"2":"abc","3":"def","4":"ghi",
           "5":"ghi","6":"mno","7":"qprs",
           "8":"tuv","9":"wxyz"}
    #const arr
    res = []
    def bfs(i,curstr):

        #base case
        if len(curstr) == len(digits):
            res.append(curstr)
            return

        #recursive call
        for c in pad[digits[i]]:
            bfs(i+1,curstr+c)

    if digits:
        bfs(0,"")

    return res


print(solution())

