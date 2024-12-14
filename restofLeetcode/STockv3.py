#same problem as always; buying/selling stock

prices = [10,1,5,6,7,1]

def solution():
    # first initlize profit; catches edge case
    prof = 0

    # create l,r pointers. The idea is that we calc for each possible combo
    l, r = 0, 1

    # now we do a while loop going until the r pointer is out of bounds. For each pointe
    # we end up calcing profit and taking max. The idea is that in the end we return max
    while r < len(prices):
        ll = prices[l]
        rr = prices[r]
        print(ll,rr)
        if ll < rr:
            proff = rr - ll
            print(proff)
            prof = max(prof, proff)
        if ll > rr:
            l = r
            r=l+1
        r += 1
    return prof

print(solution())