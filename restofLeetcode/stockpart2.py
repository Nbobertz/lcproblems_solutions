#here we have an evolution of the buying and selling stock problem. The idea here is that you can buy and sell stock across the entire array. You have to return the profit of the total array.

prices = [7,1,5,3,6,4]

def solution():
    maxp = 0
    l,r = 0,1
    for p1 in range(len(prices)):
        for p2 in range(p1 + 1, len((prices))):
            if prices[p1]<prices[p2]:
                maxp+=prices[p2]-prices[p1]
                print(prices[p2],prices[p1],prices[p2]-prices[p1])
                break



    return maxp

def solution2():
    ##the trick
    #the trick here is to calculate imediatly behind it as you aterate across the array. so 1,2,3,4 will have 1 looking at null, 2 looking at 1, 3 looking at 2 etc.

    maxprofit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            maxprofit += prices[i] - prices[i - 1]
    return maxprofit

print(solution2())