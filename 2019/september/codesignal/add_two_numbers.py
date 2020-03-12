
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = l1
        n2 = l2
        b = None
        root = None
        a = 0
        while n1 is not None or n2 is not None:
            val = n1.val if n1 is not None else 0
            val += n2.val if n2 is not None else 0
            val += a
            new_node = ListNode(val % 10)
            a = val // 10
            if b is None:
                root = new_node
            else:
                b.next = new_node
            b = new_node
            n1 = n1.next if n1 is not None else None
            n2 = n2.next if n2 is not None else None
        if a > 0:
            new_node = ListNode(a)
            b.next = new_node
        return root


add_two = Solution()
node1 = ListNode(1)
root1 = node1
node2 = ListNode(8)
node1.next = node2
# node3 = ListNode(3)
# node2.next = node3


node1 = ListNode(0)
root2 = node1
# node2 = ListNode(6)
# node1.next = node2
# node3 = ListNode(4)
# node2.next = node3


root = add_two.addTwoNumbers(root1, root2)
print(root.val, root.next.val, root.next.next.val)
