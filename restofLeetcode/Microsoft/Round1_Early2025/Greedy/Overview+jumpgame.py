#here we are given a jump game. It is an array where each point on the array is how far you can jump from that location.
#the ideal solution here is to use a greedy algorithm. With this we can simply calculate the total number of jumps it takes to
#get to the end at each spot and simply return the minimum from that location.

#greedy is a great algorithm to use if we can brute force each point in what would be a DP solution. In this case we can because the question asks just what is the mininmum amount of jumps it takes to get to the end of the array. We don't care if we go over.

nums = [2,3,0,1,4]

def solution():

    #const our variables
    jumps = 0
    n = len(nums) #keeps us from having to write it out
    current_end = 0 #keeps track of the current ending point in the array
    farthest = 0

    for i in range(n-1): #loop through all positions
        farthest = max(farthest,i+nums[i])

        if i == current_end:
            jumps +=1
            current_end = farthest
    return jumps

print(solution())