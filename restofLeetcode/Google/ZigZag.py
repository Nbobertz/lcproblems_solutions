#here we are going to be given a string and the idea is that we will then return the zig zag equivilent when given the depth of the zig zag. There is two ways to solve this problem but the most efficent one is string iteration and understanding the math behind the zig zag.

#if you get this in an interview good luck.

s = 'PAYPALISHIRING'
numRows = 3


def solution():

    #captures base case of numRows being either larger than the word or only 1 row
    if numRows == 1 or numRows>len(s):
        return s

    #construct the result function
    res = ""

    #here is where we run through the number of rows over the stirng
    for r in range(numRows):

        #increment is the number of rows that we are at.
        increment = 2 * (numRows - 1)

        for i in range(r,len(s),increment):
            res+=s[i]
            if (r>0 and r< numRows -1 and i+increment - 2 * r<len(s)):
                res += s[i+increment - 2 * r]

    return res

print(solution())