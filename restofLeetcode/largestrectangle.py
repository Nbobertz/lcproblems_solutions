#here we are going to be given an array of integers and it is our job to find the largest rectangle amoung the integers. Each unit has an area of 1. Rectangle is L*H

#Here I think the best course of action is to use a stack. We use two pointer and then take the min of the array and multiply by it's index. This we then push through each element and the largest rectangle is returned as max.

heights = [7,1,7,2,2,4]

def solution():
    maxr = 0
    for p1 in range(0,len(heights)):
        stack = []
        for p2 in range(p1+1,len(heights)):
            print(heights[p1],heights[p2])
            mins = min(heights[p1],heights[p2])
            if len(stack)==0:
                stack.append(mins)
            else:
                if mins<=stack[-1]:
                    stack.append(mins)
            print(stack[-1])


            rec = stack[-1]*p2
            maxr=max(maxr,rec)

    return maxr
#couldn't get the final condition of checking for left and right

#below is neetcode solution
def solution2():
    maxArea = 0
    stack = [] #put a pair, (index,height)

    for i, h in enumerate(heights):
        start =i
        while stack and stack[-1][1]>h:
            index,height = stack.pop()
            maxArea=max(maxArea,height*(i-index))
            start = index
        stack.append((start,h))

    for i,h in stack:
        maxArea = max(maxArea,h*(len(heights)-i))
    return maxArea





print(solution2())