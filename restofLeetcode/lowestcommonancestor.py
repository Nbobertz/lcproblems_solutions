#here we are given a binary search tree and the idea is that we have to find the low4est common ancestor. The fact that it is a binary tree should give us a hint that we have to do breath for search.

#due to this we will have to run the following code in LC as they have the test cases for trees.

def solution():
    cur = root

    while cur != None:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur


print(solution())

#this works because what we are doing is manipulating the binary tree to our advantage. We know that there will always be a - number to the left and the + to the right. We can iterate through this tree to find out where our lowest ancestor is.