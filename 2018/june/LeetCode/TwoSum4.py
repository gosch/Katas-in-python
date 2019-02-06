from generic.TreeNode import TreeNode


class Solution:
    def findTarget(self, root, k):
        """
        :param numbers:
        :param target:
        :return:
        """
        if not root:
            return False

        return self._find_target(root, set(), k)

    def _find_target(self, node, nodes, k):
        if not node:
            return False

        complement = k - node.value
        if complement in nodes:
            return True

        nodes.add(node.value)
        return self._find_target(node.left, nodes, k) or self._find_target(node.right, nodes, k)


sol = Solution()
root = TreeNode(7)
root.left = TreeNode(2)
root.right = TreeNode(11)
root.right.right = TreeNode(15)


print(sol.findTarget(root, 9))
