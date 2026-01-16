#here we are given a series of courses and asked to figure out a way to find out if the courses can be completed.
#the courses are subarrays where the 1st index is the course itself and the second is the prerequest

prerequisites = [[1,0]]
numCourses = 2

def solution():
    # build a hashmap containing the course along with empty array so that we can add the prerequestes to it
    premap = {i: [] for i in range(numCourses)}

    # build a set to keep track of evverything along the dfs path
    visit = set()

    # loop through the courses and append the pre to the hashmap
    for crs, pre in prerequisites:
        premap[crs].append(pre)

    # now we have a hashmap of all the courses with their value as the prerequestet for it.
    def dfs(crs):
        if crs in visit:  # we got a cycle in courses
            return False
        if premap[crs] == []:
            return True

        # add to visit set
        visit.add(crs)
        for pre in premap[crs]:
            if not dfs(pre): return False
        # remove from visit set
        visit.remove(crs)
        premap[crs] = []
        return True

    for crs in range(numCourses):
        if not dfs(crs): return False
    return True


print(solution())