"""
Did number of strings that appear as substring


"""

answer = 0
# just check if string 1 is in string 2
for wor in patterns:
    if wor in word:
        answer += 1

return answer