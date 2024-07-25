#the question is if I give you a string of parenthenic characters ((,),{,},[,]) can you build a program to return true of the parenthsis logically close. If they do then you can return True, else return False.

#for example; s = '(({}))'
#output = True
#or s = '()()()'
#output = True

#Constraints
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#above means that you are looking at a math problem. You can't have a (} as this would break the logic.

#sound out the brute force way.
#so when a human does this they will first read the characters left to right to see if each parenthsis is closed off by the guy to the right of it. After this the human will then see if the outside to center is closed off. For example (({})) is a parenthesis of True as it is closed properly. Also ()[]{} is True because each parenthsis is closed properly.

# I am going to use the two pointer algorithm here. First I am going to read from left to right to see if the ()[]{} is true. After this I will do the outside in approach. In reflection, it is better if we start with the outside in approach and then loop thorugh left to right.

#modules
import random,time
#Below are examples.
#below (ex1) is true
example1 = '(([{}]))'
#below (ex2) is true
example2='(){}[]'
#below (ex3) is false
example3='{[}](()('
#below (ex4) is false
example4='(([{{]}))'
#below (ex5) is false
example5='('
#below (ex6) is false
example6='()()('
#below (ex7) is True
example7='((({}{})))'
#below (ex8) is True
example8='()'
#below (ex9) is false
example9='([)]'
#below (ex10) is true
example10='()[]{}'
#belos (ex11) is false
example11='){'

#below is the setup
def setup():
    expick=random.randint(0,10)
    if expick==0:
        s=example1
        return s
    elif expick==1:
        s=example2
        return s
    elif expick==2:
        s=example3
        return s
    elif expick==3:
        s=example4
        return s
    elif expick==4:
        s=example5
        return s
    elif expick==5:
        s=example6
        return s
    elif expick==6:
        s=example7
        return s
    elif expick==7:
        s=example8
        return s
    elif expick==8:
        s=example9
        return s
    elif expick==9:
        s=example10
        return s
    elif expick==10:
        s=example11
        return s
    else:
        s=example6
        return s
def solution():
    test1=False
    test2=False
    answer=False

    #checks to see if the string is less then two characters. This makes it impossible to close the loop.Return False
    if int(len(s))<2:
        answer=False
        print('less then 2')

    #checks to see if the len of the string is odd. if it is then it returns false as there is no way of closing the parenthsis due to lack of matching mate
    if len(s)%2!=0:
        answer=False
        print('The length of s is odd')
        return answer

    if len(s)==2:
        p1=s[0]
        p2=s[1]
        if p1 == ')' or p1=='}'or p1 == ']':
            answer = False
            return answer
        if p1=='('and p2!=')':
            answer=False
            print('test1')
            return answer
        elif p1=='['and p2!=']':
            answer=False
            print('test2')
            return answer
        elif p1=='{'and p2!='}':
            answer=False
            print('test3')
            return answer
        else:
            answer=True
            print('here')
            return answer

    #perform the first two pointer check(outside to in)-test1
    counter=0
    for p1 in range(0,int(len(s))):
        counter+=1
        negcounter = counter*-1
        time.sleep(.5)
        print('p1 is at index {a}'.format(a=p1))
        print('p2 is at index {a}'.format(a=len(s)+negcounter))
        time.sleep(1)
        p2=negcounter
        print(s[p1])
        print(s[p2])
        if p1>((len(s)+negcounter)):
            answer=False
            break
        else:
            if s[p2]=='[' or s[p2]=='{' or s[p2]=='(':
                test1=False
                break
            if s[p1]==']'or s[p1]=='}' or s[p1]==')':
                test1=False
                break
            elif s[p1]=='('and s[p2]!=')':
                test1=False
                break
            elif s[p1]=='['and s[p2]!=']':
                test1=False
                break
            elif s[p1]=='{'and s[p2]!='}':
                test1=False
                break
            else:
                test1=True
    print('test1 came back as {a}'.format(a=test1))

    #now we are going to perform the other two pointer left to right technique. We check to see if test 1 came back false, if it did then we do test 2
    for counter2 in range(0,int((len(s))/2)):
        p1 = counter2 *2
        p2 = p1+1
        if s[p1] == ')' or s[p1] == '}' or s[p1] == ']':
            test2 = False
            return answer
        if s[p1]=='(' and s[p2]!=')':
            test2=False
            break
        if s[p1]=='[' and s[p2]!=']':
            test2=False
            break
        if s[p1]=='{' and s[p2]!='}':
            test2=False
            break
        else:
            test2=True
    print('test2 came back as {a}'.format(a=test2))


#test 1 is the two ponter inside to out
#test 2 is the left to right
    #if test1==True:
        #answer=True
    if test1==False and test2==False:
        answer = False
    if test1== False and test2==True:
        answer=True
    if test1==True and test2==False:
        answer=True
    return answer
#below is the calling of the functions
#s=setup()
s="(([]){})"
print(s)
answer=solution()
print(answer)