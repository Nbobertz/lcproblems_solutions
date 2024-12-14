#here we are going to be given an array of unique integers. Our goal here is to return ALL possible permutations of that array as subarrays

nums = [1,2,3]

def permute():
    res = []

    #base case
    if (len(nums)==1):
        #this catches if we are given an array of only 1 integer. Return it as a singular subarray
        return [nums.copy()]

    #now we are going too create a recursive call to pop the 0th index from nums and append it to each subarry then add it back.
    for p1 in range(len(nums)):
        n = nums.pop(0)
        perms = self.permute(nums)

        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    return res