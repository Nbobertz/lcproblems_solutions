#Here we are going to be given a string of roman numerals and the goal is to convert this to a hindu-arabic numerical system. Below are the numericals and their values

#I = 1
#V = 5
#X = 10
#L = 50
#C = 100
#D = 500
#M = 1000

# How this works: The logic is that if a smaller numbe comes before the larger one you have to subtract it. There can only be one smaller number before the larger one. EX LIV is 59 because IV is 4 and L is 50. Now XLIV is 44. The trick here is to use a hashmap to store the value of the character to replace it with arabic number. Then work right to left, if there is a smaller number before the larger one we subtract it and keep going.

s='CMLII'

def solution():
    hashmap={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    number =0
    for p1 in range(0,len(s)):
        if p1 +1 < len(s) and hashmap[s[p1]]<hashmap[s[p1+1]]:
            number-=hashmap[s[p1]]
        else:
            number+=hashmap[s[p1]]
    return number

print(solution())