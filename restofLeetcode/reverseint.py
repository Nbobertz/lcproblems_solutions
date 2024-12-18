#here we are going to be given an integer and our goal is to reverse it.

x = 123

def solution(x):
    st1 = ''

    # convert to string, find if negative and hold
    tmp = str(x)
    neg = False

    if tmp[0] == '-':
        tmp2 = list(tmp)
        tmp = ''
        tmp2.pop(0)
        neg = True
        for x in tmp2:
            tmp += str(x)

    for x in tmp[::-1]:
        st1 += x

    answer = int(st1)

    if neg == True:
        answer = (answer * -1)
    return answer

print(solution(x))


def solution2(x):
    sign = [1, -1][x < 0]
    rev, x = 0, abs(x)
    while x:
        x, mod = divmod(x, 10)
        rev = rev * 10 + mod
        if rev > 2 ** 31 - 1:
            return 0
    return sign * rev

print(solution2(x))