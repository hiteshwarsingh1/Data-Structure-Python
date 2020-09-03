class Node():
    def __init__(self,data):
        self.data = data
        self.rightNode = None
        self.leftNode = None
        #self.parent = parent
class binaryTree():
    def __init__(self):
        self.root = None
        self.num = 0

    def insert(self,data,root):
        curr = self.root
        if data < curr.data:
            if not curr.leftNode:
                new = Node(data)
                curr.leftNode = new
                print("AddedLf")
            else:
                self.insert(data,curr.leftNode)
        else:
            if not curr.rightNode:
                new = Node(data)
                curr.rightNode = new
                print("AddedRt")
            else:
                self.insert(data,curr.rightNode)

    def add(self,data):
        self.num = self.num + 1
        if not self.root:
            new = Node(data)
            self.root = new
            print("AddedRo")
        else:
            self.insert(data,self.root)

    def trav_io(self,node):
        if node.leftNode:
            self.trav_io(node.leftNode)
        print(node.data)
        if node.rightNode:
            self.trav_io(node.rightNode)

    def trav(self):
        if self.root != None:
            self.trav_io(self.root)




BT = binaryTree()
BT.add(10)
BT.add(8)
BT.add(15)
BT.trav()
