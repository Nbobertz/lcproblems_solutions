#Here we are going to be given a string and our job will be to build a script that can find if any two numbers right beside each other are the same. Ex. Hello = ll is the same pair. From this point we simply print out the letter as a string as the answer


#establish constraints
#1.) Are all of the letters lowercase or uppercase? Can they be mixed? Answer: They are all lower
#2.) Will there always be a solution or should we account for null? Answer: There won't always be a solution
#3.)What if there are multiple pairs of corrent letters? What do we print? Answer: Print the first one starting from the left most letter (ex. Bacchhuuss would be c as it is the first letter)
#4.) Can the outside letters be a pair? (ex helloh index 0 and -1 would be the hh pair). Answer: No, you can't loop around.


#Talk/write up how we would do this manually? For me the most brute force approach would be to start at the 0 index and loop through until we get a match. So for this we would establish two pointers, the first is at index position 0 and the next one is at index position 1 of the given string. We would then take the value of each letter and see if they match. If they do then we have our pair and we exit the loop. If not then we print null
#https://leetcode.com/problems/first-letter-to-appear-twice/description/
#code up the solution.

s = 'revav'
def twopointercheck():
    for let in range(0, len(s)):
        pointer1 = s[let]
        print(pointer1)
        pointer2 = s[let + 1]
        if pointer1 == pointer2:
            answer = pointer1
            return answer
        elif pointer2 == s[0]:
            answer = pointer2
            return answer
        if let+1==len(s)-1:
            return None


answer=twopointercheck()
if answer == None:
    print('There is no answer/null')
else:
    print(answer)