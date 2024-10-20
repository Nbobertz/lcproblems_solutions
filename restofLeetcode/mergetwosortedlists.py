#here we are going to be given two sorted linked lists. The idea is that the lists themselves need to be zipped up into one giant list and have that list be sorted. This problem tests if a candidate knows about linked lists and how to manage them.

def solution():
    dummy = ListNode()
    tail = dummy

    while li and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1=l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    return dummy.next
