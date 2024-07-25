#the goal here is to write a program that can check to see if a string of parenthesis characters are valid. ex (), [], {} is valid while (({())) is not.

#constraints
#there will always be a character of parenthesis in the s string. The string will always have at least one character. Answer will be bool either True or False

#brute force. Here the most brute force way of doing this is to go from left to right and store each character in the string. We see if the string is even due to matching pair, then we see if the first character is open and the last is close, if both test pass then we step into the logic. Here we want to use a stack and add each character to the top of the stack as we go from left to right only if it is an open parenthesis, if it is a closed parenthesis then we check to see if the top of the stack coresponds to it. If it does then we pop if not then we retun false.

s = '()()(){}'

#code up the solution
def solution():
    stack = []
    matchinghash = {'}':'{',']':'[',')':'('}
    for char in s:
        if char in matchinghash:
            if stack and stack[-1]==matchinghash[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return True if not stack else False

print(solution())