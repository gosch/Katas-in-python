# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def removeKFromList(l, k):
    start = l
    while l.value == k:
        l = l.next
        start = l


    while l is not None:
        while l.next is not None and l.next.value == k:
            l.next = l.next.next
        l = l.next

    return start


val1 = ListNode(3)
val2 = ListNode(1)
val3 = ListNode(2)
val4 = ListNode(3)
val5 = ListNode(4)
val6 = ListNode(5)
val1.next = val2
val2.next = val3
val3.next = val4
val4.next = val5
val5.next = val6

print(removeKFromList(val1, 3))
