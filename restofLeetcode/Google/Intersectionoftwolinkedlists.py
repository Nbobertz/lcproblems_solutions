#here we are going to be given two linked lists and it is our job to find the intersection of both of these linked lists

#run this in LC

bnodes = set()

while headB:
    bnodes.add(headB)
    headB = headB.next

while headA:
    if headA in bnodes:
        return headA
    headA = headA.next
return None