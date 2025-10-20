#redid the daily temps problem again. Starting to get the hang of monotonic stacks

class Solution(object):
    def dailyTemperatures(self, temperatures):
        #here we can use a monotomic stack. We simply need to capture the index of each spot and then add to the current

        #The idea is that we add to the stack, when we see a larger number then we pop, capture the diffrence between the two indeces, and append that to the index
        res = [0] * len(temperatures)

        #now we use a stack and pop/add to see where we are at
        stack = []

        for i in range(0,len(temperatures)):
            t = temperatures[i]
            while stack and t > stack[-1][0]:
                stemp,sindex = stack.pop() #store as tuple
                res[sindex]= i-sindex
            stack.append([t,i])
        return res