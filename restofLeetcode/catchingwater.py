#here we are going to be given an array of itegers. The whole goal here is to calculate just how much water could be trapped by a graph if each integer represented the height of a bar chart. So for example [1,2,3,0,4,5,2] there would be 3 units of water between 3,0,4. If the water rolled over the side.

#example
height = [4,2,0,3,2,5]

#constraints
#positive only numbers, side of graph is not a constraint of water.
def solution():
    if not height: return 0

    l,r = 0,len(height)-1
    leftmax,rightmax = height[l],height[r]
    res = 0

    while l<r:
        if leftmax<rightmax:
            l+=1
            leftmax=max(leftmax,height[l])
            res+=leftmax-height[l]
        else:
            r-=1
            rightmax=max(rightmax,height[r])
            res+=rightmax-height[r]
    return res

print(solution())
