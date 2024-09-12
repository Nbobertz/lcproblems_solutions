#here we are going to do the first leetcode question; two sum. Here we are going to be given an array of integers and a target integer. What we are going to do is loop through the array and find the two integers that add up to the target. If you find the target in the array then you need to print off the two index points in an array.

#constraints: There will always be two numbers in the array. Further, the numbers will always be positive.

example = [1,2,3,4,5,6]
target = 9

#below is the two pointer method using the standard brute force.

def solution():
    answer=[]
    for p1 in range(0,len(example)):
        for p2 in range(p1+1,len(example)):
            if example[p1]+example[p2]==target:
                answer.append(example[p1])
                answer.append(example[p2])
                return answer


#below we will build the hashmap solution

print(solution())
