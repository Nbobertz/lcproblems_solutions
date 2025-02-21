#here we have a stock portfolio as a list of tuples and the idea is that we have to provide an array of tuples that corespond to the value of the portfolio on any given day.

stocks = [
    [('5/1',100),('5/8',150),('5/10',200)], #msft
    [('5/1',100),('5/10',200)], #pltr
    [('5/8',50),('5/10',250)], #amzn
]

#the idea is that we should output an array that is the value of your portfolio on any given day
#ex [('5/1',200),('5/8',300),('5/10',650)]


def solution():
    ans = []

    portfolio = {}
    dates = []


    #capture everything a hashmap
    for p1 in range(len(stocks)):
        for y in stocks[p1]:
            date,price = y[0],y[1]
            if date not in dates:
                dates.append(date)
            name = "stock{a}".format(a=p1+1)
            if name not in portfolio:
                portfolio[name]=[[date,price]]
            elif name in portfolio:
                portfolio[name].append([date,price])

    print(portfolio)

    #go through and add to day array
    day = []
    for stock in portfolio:
        counter = 1
        history = portfolio[stock]



        for x in history:
            date,price = x[0],x[1]
            if date == dates[0]:
                if len(ans) == 0:
                    ans.append(price)
                else:
                    ans[0] = ans[0]+price
            else:
                for y in history:
                    if dates[counter] in y:
                        pass



    print(ans)


solution()