#here we are going to be given the degree of an array. The idea is that the degree is the number that appears the most times. We are to then take that degree and see what he smallest continus subarray is and return the len of that. This is an easy but in reality is not.

#So I think the best way to go about this is to get the degree of the array first. After that we will then see what numbers have that degree and then do sliding window to see what the smallest amount is.

#turns out you don't need to do sliding window. The easiest way to go about this is to get two hashmaps. Get the occurance of numbers in one. That is your degree then get the first index you saw this number at. Once you get to a new degree return the array length between the first time seeing and the current position. That is the len answer

nums =[1,1]

def solution():
    count={}
    end={}
    start={}

    for i in range(len(nums)):
        if nums[i] not in count:
            count[nums[i]]=1
            start[nums[i]]=i
            end[nums[i]]=i
        else:
            count[nums[i]]+=1
            end[nums[i]]=i
    result=[]
    maxi = max(count.values())
    for i,j in count.items():
        if j==maxi:
            total=end[i]-start[i]+1
            result.append(total)
    return min(result)

print(solution())