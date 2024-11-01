#Here we are going to be given a linked list and the idea is that we need to see if the linked list is in a cycle. Essentially this linked list can point back towards another node.

#there are two ways to solve this problem; either with a runner (.next.next and slow.next) or by capturing the node in a hashmap/array and returning false if you hit it again. Both are O(N) since at worse case you have to loop through every single element in the list.

# class ListNode:
#     def __init__(self,x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if head == None:
#             return False
#         slow, fast = head, head.next
#
#         while slow != None and fast != None:
#             if fast == slow:
#                 return True
#             if fast == None or fast.next == None:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
#
# print(Solution.hasCycle())

#you need to go to leetcode to test the linked list stuff as they have the constructed linked lists. The below hasCycle function is the correct code for the runner.