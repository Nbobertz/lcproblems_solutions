#here we are going to be given an array of integers. The idea is that each integer is the price of the stock and the index point is the array. Your goal here is to build a program that can easily iterate through the array and find the maximum profit that you could make if you buy/sell a stock on the days.

#the idea is that your going to use sliding window to find this. The reason we run a sliding window is that we can iterate through the array and buy/sell to record the max profit. If profit beats max then we have a new max profit. If we encounter a lower point then our left pointer then we move that to l and record the newest lowest pointer

prices = [7,1,5,3,6,4]

def solution():
    #we initilize the left and right pointer. The idea is that you will iterate with two pointers
    l,r = 0,1

    #create maxp as max profit. The idea here is that you are going to capture the maximum profit that you see within the while loop
    maxp = 0

    #run a while loop so that if r hits the end the program ends since we will have captured the maximum profit
    while r<len(prices):
        #if prices at left pointer is less then the prices at r
        if prices[l]<prices[r]:
            #calculate profit
            profit = prices[r]-prices[l]
            #calculate max-profit
            maxp=max(maxp,profit)
        #if the left pointer is less than the right pointer. Move left pointer to right pointer
        if prices[l]>prices[r]:
            l=r
        #make sure you iterate through while loop so you don't get stuck in an endless loop. r+=1 will make r eventually hit the len()
        r+=1
    return maxp

print(solution())