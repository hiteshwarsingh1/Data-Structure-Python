class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
class Stack:
    def __init__(self):
        self.head = None
        self.length = 0
#Adding Element in Stack
    def add(self,data):
        self.length = self.length + 1
        new = Node(data)
        if not self.head:
            self.head = new
        else:
            new.nextNode = self.head
            self.head = new
        print("Added Element:", data)
#Deleting Element from Stack
    def dele(self):
        curr = self.head
        self.head = curr.nextNode
        self.length = self.length-1
        print("Deleted Element:", curr.data)
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.nextNode
    def len(self):
        return self.length

Stack1 = Stack()
#Adding some elements in Stack
Stack1.add(7)
Stack1.add(5)
Stack1.add(3)
Stack1.add(2)
Stack1.add(6)
Stack1.add(9)

#Display Stack
Stack1.display()

#Deleting Elements from Stack
Stack1.dele()
Stack1.dele()

#Display Stack
Stack1.display()
