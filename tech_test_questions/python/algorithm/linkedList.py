class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def printLinkList(self, test):
        print("=== test " + test + " ===")
        node = self.head
        while(node):
            print(node.value)
            node = node.next

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            return
        node = self.head
        while(node.next):
            node = node.next
        node.next = Node(value)

    def pop(self):
        node = self.head
        while(node.next.next):
            node = node.next
        node.next = None

    def appendFront(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def popFront(self):
        if self.head == None:
            return
        self.head = self.head.next

linkList = LinkList()
# Test append.
for i in range(1, 6, 1):
    linkList.append(i)
linkList.printLinkList("append")
# Test pop.
linkList.pop()
linkList.printLinkList("pop")
# Test appendFront.
linkList.appendFront(0)
linkList.printLinkList("appendFront")
# Test popFront.
linkList.popFront()
linkList.printLinkList("popFront")