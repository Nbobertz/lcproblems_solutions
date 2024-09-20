#here we are going to do the first leetcode question; two sum. Here we are going to be given an array of integers and a target integer. What we are going to do is loop through the array and find the two integers that add up to the target. If you find the target in the array then you need to print off the two index points in an array.

#constraints: There will always be two numbers in the array. Further, the numbers will always be positive.

example = [3,2,4,2]
target = 6
print(example)
print('the target is {a}'.format(a=target))

#below is the two pointer method using the standard brute force.

def solution():
    answer=[]
    for p1 in range(0,len(example)):
        for p2 in range(p1+1,len(example)):
            if example[p1]+example[p2]==target:
                answer.append(example[p1])
                answer.append(example[p2])
                return 'the answer here is {a},{b}'.format(a=answer[0],b=answer[1])


#below we will build the hashmap solution

def solution2():
    #create the answer solution
    answer=[]
    hmap={}
    l,r = 0,len(example)
    print(l)
    print(r)
    if len(example)%2!=0:
        a = int((len(example)/2))
        hmap.update({example[a]:a})

    #below we are going to be using the two pointer algorithm. The idea is that as we loop through the array we will take the value of each integer at point l or r and then add the index point and value to the hmap dictionary(hashmap)
    while l<=r:
        hmap.update({example[l]:l})
        hmap.update({example[r-1]:r})
        print(example[l])
        print(example[r-1])

        #below we are creating the target integers based off the remainder of the l or r pointer being subtracted from the main target
        t1 = target-example[l]
        t2 = target-example[r]

        #now we create the logic to see if the t1 or t2 are in the hmap. If they are we will then append to the answer.

        #here is for left pointer check
        if t1 in hmap:
            answer.append(l)
            answer.append(hmap[t1])
            return answer
        #here is for the right pointer
        elif t2 in hmap:
            answer.append(r)
            answer.append(hmap[t2])
            return answer
        print(hmap)
        #iterate the left and right pointer for the two pointer algo
        l+=1
        r-=1


#below are the print statements
#print(solution())
print(solution2())
