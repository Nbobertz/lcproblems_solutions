#here we are given two arrays in ascending order. We are to merge both arrays and then return the first array. the final array has to be in ascending order

#I think the best case solution here would be to replace the index point of the first array if we encounter the second array point. This can be utalized in an o(N) time complexity and will result in us looping over the first list, see if any in place wee need to edit. This could also be solved with a stack. Take both pointers, one at array 1 at 0 index the other at array 2 at 0 index. Pop to two seperate stacks from end of both arrays. At the end we append to the first array.

nums1 = [1,2,0,0]
nums2 = [3]
m = 3
n = 1


#did not get the logic down. Turns out the easiest way is to simply move integers and store variables. Went to far overboard.
def solution():
    stack = []
    counter = 0
    if len(nums1)==1 and len(nums2)==0:
        pass
    elif len(nums1)==0 and len(nums2)!=0:
        nums1.append(nums2[0])
    elif len(nums2)==0:
        pass
    else:
        for x in range(0,n):
            nums1.pop()
        while len(nums2)!=0:
            if nums1[-1]<nums2[-1]:
                stack.append(nums2.pop())
            if nums1[-1]>nums2[-1]:
                stack.append(nums1.pop())
                nums1.append(nums2[-1])
                nums2.pop()
                nums1.append(stack[-1])
                stack.pop()
        for p1 in range(0,len(stack)):
            counter-=1
            nums1.append(stack[counter])


def solution2():
    midx = m-1
    nidx = n-1
    right = m+n -1

    while nidx >= 0:
        if midx>=0 and nums1[midx] > nums2[nidx]:
            nums1[right] = nums1[midx]
            midx-=1
        else:
            nums1[right] = nums2[nidx]
            nidx -= 1
        right -= 1

def solution3():
    nums1[m:] = nums2
    nums1.sort()
solution2()
print(nums1)