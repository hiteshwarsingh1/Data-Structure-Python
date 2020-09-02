class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
class Queue:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self,data):
        self.length = self.length + 1
        new = Node(data)
        if not self.head:
            self.head = new
        else:
            new.nextNode = self.head
            self.head = new
        print("Added Element:", data)

    def dele(self):
        self.length = self.length - 1
        curr = self.head
        while curr.nextNode is not None:
            prev = curr
            curr = curr.nextNode

        print("Deleted Element:", curr.data)
        prev.nextNode = None


    def display(self):
        print("___________")
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.nextNode


    def len(self):
        return self.length

Q = Queue()

Q.add(2)
Q.add(6)
Q.add(1)
Q.add(9)
Q.add(3)
Q.add(4)

Q.display()

Q.dele()
Q.dele()

Q.display()
