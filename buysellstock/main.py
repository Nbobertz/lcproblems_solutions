#here we are going to be given an array of random positive or negative integers. The idea is that the index of the array is the day of trading and the integer is the price at the index position. You need to write an algorithm that can loop through this array and figure out the best time to buy and sell to maximise profit.

#the trick here is to use a sliding window. So we have two pointers to define the maximum size of the window. If the window is positive then we add it to the maximim value and then move the window to the right until we get to the end of the array.

#array
prices = [7,1,5,3,6,4]

def solution():
    l = 0
    r = 1
    topprice = 0
    while r < len(prices):
        if prices[l] > prices[r]:
            l = r
        elif prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            if profit > topprice:
                topprice = profit
        r += 1
    return topprice


print(solution())
