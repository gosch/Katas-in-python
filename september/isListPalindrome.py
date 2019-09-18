from september import removeKFromList as nod


def check(r, l):
    if l.next is None:
        if r.value == l.value:
            return r.next
        else:
            return None
    b = check(r, l.next)
    if b is r:
        return r
    if b is None:
        return None
    if b is l:
        return r
    if b.value == l.value:
        return b.next


def check2(c, l, p):
    if c == 0:
        return l.value == p.value


def inverse_list(b, p):
    if p.next is None:
        p.next = b
        return p
    else:
        l = inverse_list(p, p.next)
        p.next = b
        return l


def isListPalindrome(l):
    # if l is None or l.next is None:
    #     return True
    # r = check(l, l.next)
    # if r is not None:
    #     return True
    # else:
    #     return False
    c = 0
    n = l
    while n is not None:
        n = n.next
        c += 1
    p = l
    i = 1
    while i < c//2:
        p = p.next
        i += 1
    p = p.next if c % 2 == 1 else p
    t = p.next
    p.next = inverse_list(t.next, t.next.next)
    t.next = None
    nod.printList(l)

l = nod.createList([1, 2, 5, 8, 5, 2, 1])
print(isListPalindrome(l))
