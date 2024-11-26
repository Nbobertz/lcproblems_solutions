#here we are given a question that we need to build a basic calculator for adding, subtracting, dividing, and multiplying. You will be given a string and have to provide back an integer that takes the valid expression

s = "3+2*2"
def solution():
    i = 0

    cur= 0
    prev= 0
    res = 0
    cur_operation = '+'

    while i<len(s):
        cur_char = s[i]

        if cur_char.isdigit():
            while i < len(s) and s[i].isdigit():
                cur = cur*10 + int(s[i])

                i +=1
            i -=1

            if cur_operation=='+':
                res += cur
                prev = cur
            elif cur_operation== '-':
                res -= cur
                prev = -cur
            elif cur_operation == '*':
                res -= prev
                res += prev * cur

                prev = cur * prev
            else:
                res -= prev
                res += int(prev/cur)

                prev = int(prev/cur)
            cur = 0
        elif cur_char != ' ':
            cur_operation = cur_char

        i +=1
    return res

print(solution())