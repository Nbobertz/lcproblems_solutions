#here we are going to be given an array of integers. There will be exactly two of every integer except for one which will only have one. It is your job to return which number has that one outlyer.

#you have to do this with linear time and memory complexity

nums = [2,2,1]

def solution():
    #so the easiest way to do this is to use the XOR operator. This operator ^= will store the number as binary and return either a 1 or 0 if the number is the same. For example the integer 5 will be a 0 and if we take another 5 this will create a 0 in bitwize since it is the same number.

    #that is the gimmick. Once you understand that it is easy to simply for loop everything and compare against the previous set int

    a = 0
    for i in nums:
        a^=i
    return a


print(solution())