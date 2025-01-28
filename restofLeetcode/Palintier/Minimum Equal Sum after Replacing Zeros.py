#here we are given two arrays with zeros and asked if we can replace zeros in them to see if we can equalize it.

nums1 = [3,2,0,1,0]
nums2 =  [6,5,0]

def solution():
    # init zero caounter for nums1 and nums2
    # these will keep track of how many 0's need to be replaced
    zero_count1, zero_count2 = 0, 0

    # init sums for both arrays
    sum1, sum2 = 0, 0

    # iterate through the first array nums1
    for num in nums1:
        if num == 0:
            zero_count1 += 1
        sum1 += num

    # iterat through second
    for num in nums2:
        if num == 0:
            zero_count2 += 1
        sum2 += num

    # create two zero counters, iterate through nums1 adding to sum and nums2 adding to sum and keeping track of zeros

    # replace all zeroes in zero count 1 and zero count 2
    sum1 += 1 * zero_count1

    # do the same for zero count 2
    sum2 += 1 * zero_count2

    # compare the two results and see if we can replace a zero to keep to the right number
    if sum1 > sum2:
        return sum1 if zero_count2 else -1

    elif sum2 > sum1:
        return sum2 if zero_count1 else -1

    return sum1