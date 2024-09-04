#At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

#Note that you do not have any change in hand at first.

#Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

#here we are going to be given an array of positive whole integers. The integers in the array represent the bill the customer gives us for our $5 lemonade. We will have to give back exact change. The customers can only pay in 5,10, and 20 alotments. The goal here is to return either False or True if we can pay out each customer or False if we cant.

#constaints
#No negative ints, there will always be a customer but inialize the answer to True just to be safe, no limit on lemonade amount, we can have money left over after the transaciton, can the first customer pay with either a 10 or 20? Yes, they can.

#example below
#bills = [5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20]

bills = [5,5,10,10,20]

#solution below
def solution():
    lefover_change = 0
    answer = True
    if bills[0]==10 or bills[0]==20:
        answer = False
        return answer
    if bills[1]==20:
        answer = False
        return answer
    for p1 in range(0,len(bills)):
        if bills[p1]==5:
            lefover_change+=5
            print('adding 5 to lefover. New value is {a}'.format(a=lefover_change))
        else:
            remainder = bills[p1]-5
            if remainder>lefover_change:
                answer=False
                return answer
            else:
                lefover_change=lefover_change-remainder
                print(lefover_change)
    return answer

#the problem is that I misinterpreted the question. We are supposed to keep track of the bills needed and not the total amount. Below is Neetcode's solution

def solution2():
    answer = True
    five,ten =0,0
    for b in bills:
        if b==5:
            five+=1
        if b==10:
            ten+=1

        change=b-5
        if change==5:
            if five>0:
                five-=1
            else:
                answer = False
                return answer
        elif change==15:
            if five>0 and ten>0:
                five,ten=five-1,ten-1
            elif five>=3:
                five-=3
            else:
                answer = False
                return answer
    return answer

print(solution2())