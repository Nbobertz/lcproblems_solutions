"""
The classic google problem. It is more of a brain teaser then anything else

The trick is to capture cur as head and then prev as None. After that you need to capture cur.next and make cur.next == prev
After that you simply update prev to cur and cur to tmp since you already pointed it next
"""


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    cur = head
    prev = None

    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    return prev