import unittest

""" This problem is from my last interview at Zenefits.  This is _my_ solution -- haven't looked for a better one. """

class Node:
    def __init__(self, name):
        self.name = name
        self.children = set()


def findbuildorder(build_in, order, record):
    for n in build_in:
        if len(n.children) == 0:
            if n.name not in record:
                record.add(n.name)
                order.append(n.name)
        else:
            findbuildorder(n.children, order, record)
            if n.name not in record:
                record.add(n.name)
                order.append(n.name)


class TestBuildOrder(unittest.TestCase):

    def test_simple(self):
        a = Node("A")
        b = Node("B")
        c = Node("C")
        a.children = (c, b)
        b.children = (c,)
        c.children = ()
        build = (a, b, c)

        theorder = []
        findbuildorder(build, theorder, set())
        self.assertEquals(['C', 'B', 'A'], theorder)

    def createNodes(self, buildin):
        nodedict = {}
        for k in buildin.keys():
            nodedict[k] = Node(k)
            
        for k, v in buildin.items():
            for dep in v:
                nodedict[k].children.add(nodedict[dep])
        
        return nodedict.values()
        
    def test_morecomplex(self):

        build_template = {
            "A": ("E", "F"),
            "B": ("G", "A", "C"),
            "C": ("E", ),
            "D": ("B", "C"),
            "E": ("G", "F"),
            "F": ("G", ),
            "G": (),
        }
        
        theorder = []
        node_list = self.createNodes(build_template)
        findbuildorder(node_list, theorder, set())
        self.assertEquals(['G', 'F', 'E', 'A', 'C', 'B', 'D'], theorder)


if __name__ == '__main__':
    unittest.main()
