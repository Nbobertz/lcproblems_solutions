#here the goal is that you will be given an integer and your whole point is to iterate the integer by one. So 1234 goes to 1235

#constraints
#so here there will always be a number between 0 and 9. Further the number can never start as a 0. You will have to return the array. Your input will be an array of inegers named digits

#brute force
#the most logical way to do this is to go to the -1 point of the array. See what number is there and then add one to it. If the number is nine then carry the 1 and make a zero.

digits = [1,2,9,9,9]
example = [4,3,2,1]
def solution():
    counter = 0
    answer = digits
    answer[-1]=answer[-1]+1
    for num in answer:
        counter +=-1
        if answer[counter]==10:
            if (counter*-1)==len(answer):
                answer[0]=0
                answer.insert(0,1)
                return answer
            else:
                answer[counter]=0
                answer[counter-1]=answer[counter-1]+1
    return answer




answer=solution()
print(answer)