# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        memory = set()
        return self.inorder(root, k, memory)

    def inorder(self, node, v, memory):
        if (v - node.val) in memory:
            return True
        memory.add(node.val)
        if node.left is not None:
            r = self.inorder(node.left, v, memory)
            if r:
                return True
        if node.right is not None:
            r = self.inorder(node.right, v, memory)
            if r:
                return True
        return False


inp = [5, 3, 6, 2, 4, None, 7]
sol = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

print(sol.findTarget(root, 9))
