#here we are given a linked list and our goal is to see if it is a palindrom. Run this in LC as they have the test examples.

def solution():
    # here we want to iterate through the linked list, print to two strings then compare
    tmp1 = []
    tmp2 = []

    curr = head

    while curr:
        tmp1.append(curr.val)
        tmp2.insert(0, curr.val)
        curr = curr.next
    print(tmp1)
    print(tmp2[::-1])

    if tmp1 == tmp2:
        return True
    else:
        return False
