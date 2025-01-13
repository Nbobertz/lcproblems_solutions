#here we are given an array and we have to find the largest outlier of the array

def getLargestOutlier(self, nums: List[int]) -> int:
    total_sum = sum(nums)

    hash_map = {}

    # iterate through array and add all elements to hashmap with it's occurance
    for item in nums:
        if item in hash_map.keys():
            hash_map[item] += 1
        else:
            hash_map[item] = 1

    # keeps track of largest outlier number
    largest_outlier = float('-inf')

    # loop through all the hashmap keys to figoure out the largest outlier
    for sum_element in hash_map.keys():

        # keep track of potential outlier. Here is the magic of the problem. We only need to keep track of the sum element times 2 and then subtract the total sum from that to get the potential outlier. If we do then we simply need to see if it's in the hashmap.keys()
        potential_outlier = total_sum - (2 * sum_element)

        # the potential outlier has to be unique and greater then 1.
        if potential_outlier in hash_map.keys():
            if potential_outlier != sum_element or hash_map[sum_element] > 1:
                largest_outlier = max(potential_outlier, largest_outlier)

    return largest_outlier