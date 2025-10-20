"""
Here we are addign two numbers together and then turning it into a linked list


"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # first read numbers into array
        arr1, arr2 = [], []

        # now read
        head1 = l1
        while head1:
            arr1.append(head1.val)
            head1 = head1.next

        head2 = l2
        while head2:
            arr2.append(head2.val)
            head2 = head2.next

        # now turn into ints
        arr1_s = ""
        for n in arr1[::-1]:
            arr1_s = arr1_s + str(n)

        arr2_s = ""
        for n in arr2[::-1]:
            arr2_s = arr2_s + str(n)

        n1 = int(arr1_s)
        n2 = int(arr2_s)

        # get full int
        fint = n1 + n2
        fint = [int(digit) for digit in str(fint)]

        # now build linked list inverse
        dummy = ListNode(0)
        curr = dummy
        for d in fint[::-1]:
            curr.next = ListNode(d)
            curr = curr.next

        return dummy.next