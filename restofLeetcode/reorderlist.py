#here we are given a head of a singly linked list. our goal is to reaarnge this into an alternating list (0,5,1,4,2,3). We do this by doing three things; first we have a fast pointer and a slow pointer to transcend the list. The slow pointer moves by 1 and the fast pointer moves by 2. The idea is that what the fast pointer hits null we have a halfway linked list at slow pointer index. The idea after this is to modify the linkage between the nodes to point towards the correct nodes then return the list.

def solution():
    #find middle
    slow,fast = head,head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    #reverse second half
    second = slow.next
    slow.next = None
    prev =None
    while second:
        tmp=second.next
        second.next = prev
        prev = second
        second = tmp

    #merge two halves
    first,second = head,prev
    while second:
        tmp1,tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first=tmp1
        second=tmp2