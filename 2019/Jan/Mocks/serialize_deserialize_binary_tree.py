from Jan.Mocks.TreeNode import TreeNode


class Codec:

    def get_pending_nodes(self, node_list):
        result = ""
        elements = [None] * (len(node_list)*2)
        pointer = 0
        flag = False
        for current_node in node_list:
            if current_node is not None:
                result += str(current_node.val) + ","
                elements[pointer] = current_node.left
                elements[pointer + 1] = current_node.right
            else:
                result += "None,"
                elements[pointer] = None
                elements[pointer + 1] = None
            flag = (elements[pointer] is not None or elements[pointer + 1] is not None) or flag
            pointer += 2

        result = result + self.get_pending_nodes(elements) if flag else result[:-1]
        return result

    def serialize(self, root: TreeNode):
        node_list = [root]
        result = self.get_pending_nodes(node_list)
        return result

    def deserialize(self, data):
        values = data.split(",")
        root = TreeNode(values[0])
        start = 1
        end = 3
        lvl = 1
        node_list = [root]
        while start < len(values):
            new_list = []
            for i in range(start, end, 2):
                value1 = values[i]
                value2 = values[i+1]
                if value1 != "None":
                    node1 = TreeNode(value1)
                else:
                    node1 = None
                if value2 != "None":
                    node2 = TreeNode(value2)
                else:
                    node2 = None
                current_node = node_list.pop(0)
                current_node.left = node1
                current_node.right = node2
                new_list.append(node1)
                new_list.append(node2)
            node_list = new_list
            start = end
            lvl += 1
            end = start + 2**lvl
        return root









# Your Codec object will be instantiated and called as such:
r = TreeNode(1)
# left = TreeNode(2)
# right = TreeNode(3)
# r.left = left
# r.right = right
# r.right.left = TreeNode(4)
# r.right.right = TreeNode(5)

codec = Codec()
res = codec.serialize(r)
# des = codec.deserialize("1,2,3,None,None,4,5")
print(res)

