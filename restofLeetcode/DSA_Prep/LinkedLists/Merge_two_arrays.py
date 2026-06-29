"""
Here we want to merge two sorted arrays. The idea here is that we want to be able to merge both teh arrays and then return as a linked list
"""
def solution(list1,list2):
    if not list1:
        return list2
    if not list2:
        return list1

    tmp = []

    while list1:
        tmp.append(list1.val)
        list1 = list1.next

    while list2:
        tmp.append(list2.val)
        list2 = list2.next

    tmp.sort()

    head = ListNode(tmp[0])
    cur = head

    for i in range(1, len(tmp)):
        cur.next = ListNode(tmp[i])
        cur = cur.next

    return head