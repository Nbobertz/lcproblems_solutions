#the idea here is that we will be given k amount of linked lists and we have to sort them into one linked list. The problem is figuruing out how to use a heap and build a linked list.

#run this on LC as the linked lists are given on there.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # use a max heap to pop into the and pull out of once everything is set up.

        arr = []

        for k in lists:
            head = k
            while head:
                var = (head.val * -1)
                heapq.heappush(arr, var)
                head = head.next

        # now pop out of heap into answer arr
        answer = []
        while arr:
            num = (heapq.heappop(arr)) * -1
            answer.insert(0, num)

        # build a listnode and assign values
        cur = dummy = ListNode(0)
        for x in answer:
            cur.next = ListNode(x)
            cur = cur.next

        return dummy.next