class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.num = 0
## ADD AT BEGIN
    def add(self,data):
        self.num = self.num+1
        new=Node(data)
        if not self.head:
            self.head = new
        else:
            new.nextNode = self.head
            self.head= new
## ADD AT END
    def append(self,data):
        self.num = self.num+1
        new = Node(data)
        a_node = self.head
        while a_node.nextNode is not None:
            a_node = a_node.nextNode
        a_node.nextNode = new
## ADD AT Position
    def insert(self,data,pos):

        new = Node(data)
        cur = self.head

        if pos > self.num:
            print("index out of range")
        else:
            while(pos-1):
                cur = cur.nextNode
                pos = pos - 1
            new.nextNode = cur.nextNode
            cur.nextNode = new
        self.num = self.num + 1
## DEL AT BEGIN
    def pop(self):
        self.num = self.num-1
        cur = self.head
        self.head = cur.nextNode
## DEFL BY ELEMENT
    def remove(self,elem):
        self.num = self.num-1
        cur = self.head
        if cur.data == elem:
            self.head = cur.nextNode
            return
        while cur.data != elem:
            prev = cur
            cur = cur.nextNode
        prev.nextNode = cur.nextNode
# DEL AT END
    def dele(self):
        self.num = self.num-1
        cur = self.head
        while cur.nextNode is not None:
            prev = cur
            cur = cur.nextNode
        prev.nextNode = None
# DEL BY POS
    def del_pos(self,pos):

        cur = self.head
        if pos == 1:
            self.num = self.num -1
            self.head = cur.nextNode
            return
        if pos > self.num:
            print("index out of range")
        else:
            while(pos-1):
                prev = cur
                cur = cur.nextNode
                pos = pos - 1

            prev.nextNode = cur.nextNode

# DISPLAY LIST
    def display(self):
        a_node = self.head
        while a_node is  not None:
            print(a_node.data)
            a_node = a_node.nextNode
# LIST LENGTH
    def length(self):
        return self.num
