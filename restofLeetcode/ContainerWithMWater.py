#here we are going to be given an array of integers named height. Our goal is to find which two integers which whne used to create a bar chart can hold the most water if we poured water over the graph. For exaple an array of 0,2,3,4,0,4,3,2 will have a container that can hold water between spaces 2 and 2.

#data structure: Here we are going to be using an array.

#algorithm: Two pointer is the proper algorithm

#brute force method. I think the brute force method here would be to have two pointers. First is at 0, and the second is at len(array) or the end. We calculate the water in the array if it was dropped between these two points and save that value. If the value is max over the previously saved one then we have the proper answer. Do this until you have done them all.

height = [1,8,6,2,5,4,8,3,7]

def solution():
    wmax = 0
    l,r = 0,len(height)-1

    #here we are calculating the area of a square over and over again (l*h). We capture L and H of each point and then calculate the area. We then move the l pointer or r pointer depending on which is smaller. The reason why is because we always want the largest pointer for the tallest square.


    while l<r:
        distance = ((r+1)-(l))-1
        minh=min(height[l],height[r])
        container = distance*minh
        wmax=max(container,wmax)

        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return wmax

print(solution())
