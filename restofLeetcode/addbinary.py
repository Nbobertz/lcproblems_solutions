#here we are going to be given two integers and we have to return their sum as binary

#for adding in binary we only get 1's and 0's. A 1 can be added to a 0 but a 1 added to a 1 will result in a cary. Ex. 11+1 = 100. This is because we have 11+1 which normal would be 12. However since the 1's place is a 1 and we are adding 01 the 1's place cancels out to a 0 and the 1 get's carried over. Now we have 10 with a 1 going into the tens place. Now it is a 1+1 which cancels out so now we have a 00 and carry the 1 over is a 100

a = '11'
b = '1'

#return answer as string
def solution(a,b):
    res = ''
    carry = 0

    a,b = a[::-1],b[::-1]

    for i in range(max(len(a),len(b))):
        digitA = ord(a[i])-ord('0') if i<len(a) else 0
        digitB = ord(b[i])-ord('0') if i<len(b) else 0

        total = digitA +digitB + carry
        char = str(total%2)
        res = char + res
        carry = total //2

    if carry:
        res = '1' + res
    return res

print(solution(a,b))
