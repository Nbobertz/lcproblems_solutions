#leetcod 1249
#here we are given a string with parenthesis randomely sprinkled within it. Our job is to write a probram that can easily remove parenthesis until we get the minimum viable solution. Looks like all we have to do is make it work. Had we have to find the minimum amoutn removedd then it would be a dp problem; here if we are given 'lee(t(c)o)de)' the last ')' would be removed to make a viable solution. Return this.

#brute force. Simply pass over with a stack from left to right. Build hashmap; assign values to closed parenthesis. If bracket is a closed one then we look to see if the partner is open. If it is we continue. if not then we pop. Convert to string, pop, return to string.

#below is the test example
s = "))stst(ts)(s()"

#below is my solution
def solution():

    #convert s to list
    ls = list(s)
    #just looking for parenthesis, if problem was expanded to other characters then we put match below
    hmap={')':'('}

    #below is stack
    stack = []

    #now we build stack and loop through adding necessary open to it and poping if we hit closed. If we don't get an open or find an open without a pair then we pop.

    #building temp word for working. replace ls later due to list comphrension
    temp = ''


    #now for the loop
    letter = False
    index = 0
    for char in ls:
        index +=1
        if char == ')' and len(stack)==0:
           continue
        if char in hmap:
            if len(stack)!=0 and stack[-1]==hmap[char]:
                stack.pop()
                temp+=char
        if char == '(':
            onlyone=True
            stack.append(char)
            for p1 in range(index,len(ls)):
                if ls[p1]==')':
                    onlyone = False
            if onlyone==False:
                temp+=char

        if char not in hmap and char != '(':
            temp+=char
            letter = True

    if letter == False:
        answer = ''
        return answer
    else:
        return temp


#couldnt get the one edge case down. Turns out you dont need a stack just to iterate over the array twice
def solution2():
    res = []
    cnt = 0
    for c in s:
        if c =='(':
            res.append(c)
            cnt+=1
        elif c ==')' and cnt>0:
            res.append(c)
            cnt-=1
        elif c!= ')':
            res.append(c)

    #second pass
    filt = []
    for c in res[::-1]:
        if c =='(' and cnt > 0:
            cnt -=1
        else:
            filt.append(c)
    return "".join(filt[::-1])


print(solution2())
