#here we are going to be given a linked list. Our goal is to reverse the list and return that.


head = [0,1,2,3]


#below is the nick solution. Was not correct because it just assumes a normal array
def solution():
    answer =[]
    counter =0
    for p1 in range(0,len(head)):
        counter-=1
        answer.append(head[counter])
    return answer

#below is two pointer solution
def solution2pointer():
    prev,curr=None,head

    while curr != None:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    return prev

print(solution2pointer())


#the reason why the above algorithm works is because in every language buy Python an array has to be constructed with a fixed length with index positions. Most of these array's are linked together via index point. Index point 1 is linked to 2 is linked to 3 is linked to 4. We use encapsultion above to push the next to a tmp variable and then inverse the seletion. After we move next.