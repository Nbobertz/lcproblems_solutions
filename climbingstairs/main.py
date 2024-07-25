#here we are going to design a script that can count how many distinct ways you can climb a staircase. You are going to be given an integer 'n' that represents the amount of stairs in the staircase. You can only climb one stair or two stairs at a time. For a staircase of 3 stairs that means you can climb it 3 diffrent ways. 1+1+1, 1+2, 2+1

#your goal here is to design a proram that can figure out how many diffrent ways you can climb this staircase

#constraints
#There will always be an answer. The integer n can be between 1 and 45. The integer will always be positive. You have to climb the entire staircase

#code it up
n = 5

def solution():
    if n == 1:
        answer = 1
        return answer
    elif n== 0:
        answer = 0
        return answer
    else:
        stairs = n+1
        dparray=[]
        counter = 0
        dparray.append(1)
        dparray.append(1)
        for x in range(0,stairs-2):
            dparray.insert(x,0)
        for num in range(0,stairs):
            counter+=-1
            if (counter*-1)==stairs:
                dparray[0]=dparray[1]+dparray[2]
                answer = dparray[0]
                return answer
            elif counter == -1 or counter == -2:
                continue
            else:
                dparray[counter] = dparray[counter + 1] + dparray[counter + 2]




answer=solution()
print(answer)