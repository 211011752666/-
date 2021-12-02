class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None

class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)
    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node
    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val <p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return
    def preOrder(self,tree):
        if tree:
            print(tree.data, end=' ')
            self.preOrder(tree.lchild)
            self.preOrder(tree.rchild)

    def posOrder(self, tree):
        if tree:
            self.posOrder(tree.lchild)
            self.posOrder(tree.rchild)
            print(tree.data, end=' ')

    def inOrder(self, tree):
        if tree:
            self.inOrder(tree.lchild)
            print(tree.data, end=' ')
            self.inOrder(tree.rchild)
tree = BST([4,6,7,9,2,1,3,5,8])
tree.inOrder(tree.root)
print()
tree.preOrder(tree.root)