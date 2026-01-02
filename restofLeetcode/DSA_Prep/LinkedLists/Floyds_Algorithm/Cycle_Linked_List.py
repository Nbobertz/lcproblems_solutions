"""
This is the classic of if there is a cycle in a linked list. We create a dummy node and make the slow the firs and the fast the next.


"""

if not head:
    return False

dummy = ListNode()
dummy.next = head
slow = fast = dummy

while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

    if slow == fast:
        return True

return False