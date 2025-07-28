#here we are given a list of numbers and have the find the longest continual incremental series of numbers

#Hard problem to understand but easy one to code up. I would not ask this in an interview as it relies upon good communication and not intution.

nums = [1,3,2,2,5,2,3,7]

def solution():
    hm = {}

    for num in nums:
        if num not in hm:
            hm[num] = 1
        elif num in hm:
            hm[num] += 1

    # now we go through and see if we have have the positive key number. If we do then we add the value to the longest because we can do [1,2,3,4,5,5,6]

    longest = 0
    for key in hm:
        if key + 1 in hm:
            longest = max(longest, hm[key] + hm[key + 1])

    return longest

print(solution())