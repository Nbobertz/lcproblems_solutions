#here the idea is that you will be given an array of whole positive integers. The integers represent days in which you can buy a stock and their price. For example, [1,3,4,2,44,3] would be the days index 0 is day 1 and the stock price is 1 while on day 3 (index 2) the price is 4.

#constraints
#so every integer is positive; can't have a negative number here. The array can be any length greater then zero. the numbers are whole.

#brute force
#so I think the best brute force solution here is to loop through the array and find the lowest number. Then look for the largest number to the right and calculate remainder from day 2 - day 1. The largest range is the output

prices = [7,1,5,6,4]

def solution():
    max = 0
    for p1 in range(0,len(prices)):
        for p2 in range(p1+1,len(prices)):
            rtest = prices[p2]-prices[p1]
            if rtest>max:
                max = rtest
    return max

answer = solution()
print(answer)