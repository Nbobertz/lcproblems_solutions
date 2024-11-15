#here we are going to be given a binary search tree and the goal is to find the lowest common ancestor. Since it is a binary search tree we can simply look to the right or the left to find the lowest common ancestor.

#run on LC since they have the exmaples

# cur = root
#
# while cur != None:
#     if p.val > cur.val and q.val > cur.val:
#         cur = cur.right
#     elif p.val < cur.val and q.val < cur.val:
#         cur = cur.left
#     else:
#         return cur