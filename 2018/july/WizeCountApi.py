from collections import OrderedDict

class Node:
    def __init__(self, name=None):
        self.name = name
        self.children = OrderedDict()
        self.counter = 0


def add_children(children, prefix):
    res = []
    for key in children:
        res.append(prefix + '--' + children[key].name + ' (' + str(children[key].counter) + ')')
        if children[key].children:
            res = res + (add_children(children[key].children, prefix+'--'))[:]
    return res




def countAPI(calls):
    root = Node('root')
    result = []
    for i in calls:
        data = i.split('/')
        del data[0]
        parent = None
        if data[0] in root.children:
            root.children[data[0]].counter += 1
            parent = root.children[data[0]]
        else:
            node = Node(data[0])
            node.counter = 1
            root.children[data[0]] = node
            parent = node

        if data[1] in parent.children:
            parent.children[data[1]].counter += 1
            child = parent.children[data[1]]
        else:
            node = Node(data[1])
            node.counter = 1
            parent.children[data[1]] = node
            child = node

        if data[2] in child.children:
            child.children[data[2]].counter += 1
        else:
            node = Node(data[2])
            node.counter = 1
            child.children[data[2]] = node

    for key in root.children:
        result.append('--' + root.children[key].name + ' (' + str(root.children[key].counter) + ')')
        if root.children[key].children:
            result = result + add_children(root.children[key].children, '--')[:]
    return result



print(countAPI([
        "/project1/subproject1/method1",
        "/project2/subproject1/method1",
        "/project1/subproject1/method1",
        "/project1/subproject2/method1",
        "/project1/subproject1/method2",
        "/project1/subproject2/method1",
        "/project2/subproject1/method1",
        "/project1/subproject2/method1"
]))

