"""
This is about merging strings alteratnivly, one character at a time
"""

answer = ''
if not word1 or not word2:
    return answer

if len(word1) >= len(word2):
    l = 0
    while l <= len(word2) - 1:
        answer += word1[l]
        answer += word2[l]
        l += 1
    answer += word1[l:]
    return answer

else:
    l = 0
    while l <= len(word1) - 1:
        answer += word1[l]
        answer += word2[l]
        l += 1
    answer += word2[l:]
    return answer