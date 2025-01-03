#this one is easy; just best time to buy and sell stock. However, it is with the range between elemetns (profit).

#nums = [1,5,2,10]
#nums = [999,997,980,976,948,940,938,928,924,917,907,907,881,878,864,862,859,857,848,840,824,824,824,805,802,798,788,777,775,766,755,748,735,732,727,705,700,697,693,679,676,644,634,624,599,596,588,583,562,558,553,539,537,536,509,491,485,483,454,449,438,425,403,368,345,327,287,285,270,263,255,248,235,234,224,221,201,189,187,183,179,168,155,153,150,144,107,102,102,87,80,57,55,49,48,45,26,26,23,15]
nums=[7,1,5,4]

def solution():
    # this is the same as sliding window. Essentially we are going to simply initiate the l,r pointers and then move them and capture an output across the array.

    # capture base case
    answer = -1

    # pointers
    l, r = 0, 1
    print(nums)
    while r <= len(nums)-1:  # essentialy while it is not at the end

        # capture if nums at l is smaller
        if nums[l] < nums[r]:
            rrange = nums[r] - nums[l]
            answer = max(rrange, answer)
            print(nums[l],nums[r],answer)
            r+=1
            l+=1
        # found that l is smaller
        elif nums[l] > nums[r]:
            l = r
            r+=1
        else:
            r+=1
    return answer

print(solution())