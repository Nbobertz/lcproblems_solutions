"""
Here we are breaking up an array into subarrays

"""


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        #build one giant array, will be o(n)
        if not grid or k == None:
            return 'None'

        bigg = []
        for i in grid:
            for n in i:
                bigg.append(n)

        #shift by k
        for n in range(k):
            tmp = bigg.pop()
            bigg.insert(0,tmp)

        #now go through and build new array
        answer = []
        #append buckets to array
        buclen = len(grid[0])
        for x in range(len(grid)):
            answer.append([])

        #now add to each sub until you hit buck len
        buc = 0
        count = 0
        while buc <= len(answer):
            #check to see if count is divisible by buclen
            try:
                answer[buc].append(bigg[count])
                count+=1
            except:
                pass
            if count >= len(grid[0]) and buc == 0:
                buc+=1
            elif count % len(grid[0]) == 0:
                buc +=1

        return answer