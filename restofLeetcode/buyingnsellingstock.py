#standard buying/selling stock program. The idea is that you are given an array of integers where the index point represents both the day and the price on that day. Here you want to write a program that can calculate the maximum profit of that timewindow for you to buy and sell the stock

prices = [7,6,4,3,1]

def solution():
    l,r = 0,1 #build the right pointer right in front of the left to start
    maxprofit = 0

    while r<len(prices):
        # is the transaction profitable?
        if prices[l]<prices[r]:
            profit = prices[r]-prices[l]
            maxprofit=max(maxprofit,profit)
        else:
            l=r
        r+=1
    return maxprofit


print(solution())