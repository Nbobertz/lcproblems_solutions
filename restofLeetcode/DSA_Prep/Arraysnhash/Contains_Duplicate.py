#here we are given an array and we need to loop through and see if there is any dupicate in the array. If there is we need to return True otherwise if the entire array containes duplicate integers then return False

#ex

#[1,2,3,4] would return False
#[1,1,2,2,3,3] would return True

#below is the solution

class solution:
    def solution(array):
        hashmap = {}

        #loop through and see if the number is in the hashmap if it is not then we add it.

        for num in array:
            #catch to see if it is in array
            if num in hashmap:
                return True
            else:
                hashmap[num]=1

        #return false if we get here
        return False


nums = [1,2,3,4,5,6]

answer = solution.solution(array = nums)

print(answer)