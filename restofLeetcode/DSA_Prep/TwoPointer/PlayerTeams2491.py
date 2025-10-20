"""
Here we want to divide players in the teams of equal skill and return the product of those teams. I got this problem done all by myself

"""

class Solution(object):
    def dividePlayers(self, skill):
        answer = None

        #what happens if we sort and pop from the top and bottom
        new = sorted(skill)

        l,r = 0,len(new)-1
        power = set()
        while l<r:
            team = new[l]+new[r]
            power.add(team)

            #temporarily add power
            if answer == None:
                answer = (new[l]*new[r])
            elif answer != None:
                answer = answer + (new[l]*new[r])
            l+=1
            r-=1

        if len(power)!=1:
            return -1
        elif len(power) == 1:
            return answer

