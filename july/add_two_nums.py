# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def __init__(self):
        super()

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = 0
        n1 = l1
        n2 = l2
        magnitude = 0
        carry = 0
        while n1 is not None or n2 is not None or carry > 0:
            val1 = n1.val if n1 is not None else 0
            val2 = n2.val if n2 is not None else 0
            cur = val1 + val2 + carry
            result += cur % 10 * 10**magnitude
            carry = cur // 10
            n1 = n1.next if n1 is not None else None
            n2 = n2.next if n2 is not None else None
            magnitude += 1

        result_str = str(result)
        size = len(result_str)

        root = ListNode(result_str[size - 1])
        n1 = root
        for i in range(size - 2, -1, -1):
            n1.next = ListNode(result_str[i])
            n1 = n1.next

        return root

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    node1 = ListNode(9)
    node2 = ListNode(6)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3
    root1 = node1

    node1 = ListNode(4)
    node2 = ListNode(5)
    node1.next = node2
    node3 = ListNode(6)
    node2.next = node3
    root2 = node1


    sol = Solution()
    result = sol.addTwoNumbers(root1, root2)
    while True:
        print(result.val)
        result = result.next
        if result is None:
            break

