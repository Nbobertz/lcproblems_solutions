#here we are given two strings of numbers. The idea is that we need to multiply them together and return the product. I did this the first time by simply converting to int and multiplying.

num1 = "2"
num2 = "3"

def solution():
    # convert str to int
    nnum1 = int(num1)
    nnum2 = int(num2)
    # mult
    answer = nnum1 * nnum2
    # convert to string
    stnum = str(answer)
    return stnum

print(solution())