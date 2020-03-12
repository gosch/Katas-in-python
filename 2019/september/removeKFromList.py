# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def removeKFromList(l, k):
    while l is not None  and l.value == k:
        l = l.next
    if l is None:
        return None

    c = l.next
    b = l
    while c is not None:
        if c.value == k:
            b.next = c.next
        else:
            b = c
        c = c.next
    return l


def createList(list1):
    b = ListNode(list1[0])
    r = b

    for i in range(1, len(list1)):
        n = ListNode(list1[i])
        b.next = n
        b = n
    return r

def printList(list1):
    c = list1
    while c is not None:
        print(c.value)
        c = c.next

if __name__ == 'main':
    list1 = [1000, 1000]
    l = createList(list1)

    printList(removeKFromList(l, 1000))
