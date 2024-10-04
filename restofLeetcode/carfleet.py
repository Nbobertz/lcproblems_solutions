#here we are going to be given two array's. THe first is the position of cars at milage towards destinaiton. ex [1,4] would be car one at mile 1 and car 2 at mile 4. The next array is speeds assigned to the cars [3,2] would mean the car one at milage 1 is going 3 mph while car 2 is going at 2 mph. Finally you will be given an integer that is the end of the road.

#your goal is to write a program that can determine how many 'fleets' of cars show up at the destination at a time. A fleet is more then one car. You can think of it as a group.

#hint this is a stack problem. Find the diffrence between the two cars in speed and then see if they will collide before hitting the end. If they do they are a group/fleet of cars.

#example below

target = 10
position=[10,8,0,5,3]
speed = [2,4,1,1,3]

def solution():
    #take both array's and zip them up into one array. Makes working with it easier
    pair = [[p,s] for p,s in zip(position,speed)]

    #now we build the stack we will add cars to as we go from -1 in stack to the front
    stack = []


    for p,s in sorted(pair)[::-1]:#reverse sorted order instanlty makes this O(logn) not efficent but get's job done.

        #now we append the car to the stack. However we are apppending the distance till the target (target -p)/s. This gives us the units of time it will take to get to the destination.
        stack.append((target-p)/s)

        #below is the magic. Here we assume there will always be a car in stack. If the new car in the stack [-1] is less time than the first we can see it is going to collide with the first car before desitnation. We then pop from the stack and assume that the first car is not a car group/fleet.
        if len(stack)>=2 and stack[-1]<=stack[-2]:
            stack.pop()

    #answer is just the amount of cars/fleets left in the stack. A singular car can be a fleet btw.
    answer = len(stack)
    return answer

answer = solution()
print(solution())