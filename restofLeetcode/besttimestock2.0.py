#here we are going to be writing a program that will determine what the best time to buy and sell stock would be. You can buy stock and then you have to sell it in the future. The idea is that if you are given an array of prices where ith index is the price of the stock on the ith day. ex. [0,2,3,1,2] the 2nd index the price on that day would be $2. The idea is that here we are going to build a program that will return the maximum you could possible achinve in the entire array. [0,2,3,1,2] the maximum price would be 3 since you can buy it on the first day (0) and sell it on the 3rd day (3).
#import globals
import time, random
#build the setup to automatically create the prices array

def setup():
    prices = []
    arrlen = random.randint(3,20)
    for x in range(arrlen):
        tmpnum = random.randint(0,1000)
        prices.append(tmpnum)

    print(prices)
    return prices



def solution():
    #here the best algorithm to use is sliding window. This means we can have two pointers and we move from left to right across the array; we move pointers based off logic.


    #init max prices var to keep track of whatever the max is.
    maxp=0
    #build two pointers, left pointer is at 0, right pointer is at 0.
    l,r = 0,1

    #now we init the whiile loop. While r> the len(prices)-1 (real array).

    while r<=len(prices)-1:

        #capture if prices at l is smaller then prices at r. Means we can get profit from the sale. We calculate if it's above hte max price
        if prices[l]<prices[r]:
            #get max between maxp and make new max
            maxp = max(maxp,prices[r]-prices[l])

        #we found a smaller price to the right. Move the left pointer to that location. This move takes place becuase we can find a larger delta.
        elif prices[l]>prices[r]:
            #move pointer
            l=r

        #capture if prices are the same
        elif prices[l] == prices[r]:
            #skip; no profit or moving of pointer
            continue

        r+=1
    return maxp
prices = setup()
print(solution())