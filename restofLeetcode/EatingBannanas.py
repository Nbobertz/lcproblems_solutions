#here we are going to be given an array and an integer (piles, and hours). The idea is that you are going to decide how long you can spend on each pile of bannanas while getting through the entire set in your specified hour requirment.

#for example:
#if your piles of bannanas are [1,4,3,2] you have 4 pies. The first pile containes 1 bannana, the second 4, and the third 3. The amount of hours you can spend eating your bannanas is 9. The trick however is you cant pick up and move until your banna pile is done. You can determine how many bannanas per hour you can eat but you must finish the pile. Your goal here is to return the minimum size of bannanas per hour you can eat while finishing the entire pile.

#How to get it done
#So I think the best brute force solution here would be to take your highest number in the array and then create a range. Put each number in an array and do binary search to see what the minimum amount of bannanas you can eat per hour and stay within the hourly rate. This should be extremly efficent.

#examle1
# piles = [3,6,7,11]
# h = 8

#example2
piles = [30,11,23,4,20]
h = 6


#could not get the one edge case down. Had a solution that pretty much worked but failed on a -1 point check
def solution():
    #here we are going to initilize the l pointer at min of piles and r at max of piles
    l,r = min(piles),max(piles)

    #create min variable to keep track
    minbannanaperhour = 0


    #now we do binary search to see if we can eat the piles while staying within the hours
    while l<=r:
        #create diff to mark middle point between pointers
        diff = int((l+r)/2)

        #capture minimum amount of bannanas per hour and still finish stack
        timetoeat = 0
        for p1 in range(0,len(piles)):
            counter = 0
            tmp =piles[p1]
            while tmp>=0:
                tmp=tmp-diff
                counter+=1
            timetoeat+=counter



        #printing for testing
        # print(l,r)
        # print(timetoeat,h)
        # print(diff)
        # print('----')

        #below is logic to move pointers
        if timetoeat <= h:
            r = diff-1
        if timetoeat >= h:
            l = diff+1
            minbannanaperhour = max(diff, minbannanaperhour)

    #now we perform one last check with one point back from diff to fine-tune the walk back to ensure the proper integer is caught
    time2eat = 0
    walkback = diff
    while walkback!=0:
        checkdiff = walkback-1
        time2eat = 0
        for p1 in range(0,len(piles)):
            counter = 0
            tmp =piles[p1]
            end = False
            while end != True:
                tmp=tmp-checkdiff
                counter+=1
                print(checkdiff, counter, piles[p1], tmp)
                if tmp <= 0:
                    print('here')
                    end = True
            time2eat+=counter
        if time2eat <h:
            print('here')
            minbannanaperhour=min(checkdiff,minbannanaperhour)
        if time2eat >h:
            break


    return  minbannanaperhour


#below is the neetcode solution
def solution2():
    import math
    l,r = 1,max(piles)
    res = r

    while l<=r:
        k=(l+r)//2
        hours = 0
        for p in piles:
            hours+= math.ceil(p/k)

        if hours <=h:
            res = min(res,k)
            r = k-1
        else:
            l = k+1

    return res
print(solution2())