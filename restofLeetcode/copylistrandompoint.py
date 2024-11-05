#here we are going to be given a random linked list with the next variable and a random pointer.

oldcopy = {None: None}

curr = head
while curr:
    copy = Node(curr.val)
    oldcopy[curr] = copy
    curr = curr.next

curr = head
while curr:
    copy = oldcopy[curr]
    copy.next = oldcopy[curr.next]
    copy.random = oldcopy[curr.random]
    curr = curr.next
return oldcopy[head]