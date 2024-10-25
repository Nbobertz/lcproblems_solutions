#here we are going to be given two strings (word1 and word2) the idea is that you will merge both strings in an alternative order w1,w2,w1,w2,w1. If at the end one string is longer then the other append it to the end of the list

word1 = 'abcded'
word2 = 'pq'

def solution():
    ww1 = list(word1)
    ww2 = list(word2)
    al = []
    answer = ''

    if len(ww1)<len(ww2):
        for p1 in range(0,len(ww1)):
            al.append(ww1[p1])
            al.append(ww2[p1])
        for p1 in range(len(ww1),len(ww2)):
            al.append(ww2[p1])
        for p1 in range(0,len(al)):
            answer+=str(al[p1])
    if len(ww1)==len(ww2):
        for p1 in range(0,len(ww1)):
            al.append(ww1[p1])
            al.append(ww2[p1])
        for p1 in range(len(al)):
            answer+=str(al[p1])
    if len(ww1)>len(ww2):
        for p1 in range(0,len(ww2)):
            al.append(ww1[p1])
            al.append(ww2[p1])
        for p1 in range(len(ww2),len(ww1)):
            al.append(ww1[p1])
        for p1 in range(0,len(al)):
            answer+=str(al[p1])
    return answer

print(solution())