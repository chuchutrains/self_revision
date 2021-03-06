class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
        self.size = 0

    def printLinkList(self, test):
        print("=== test " + test + " ===")
        node = self.head
        msg = ""
        while(node):
            if node.prev:
                msg += str(node.prev.value)
            msg += " <- " + str(node.value) + " -> "
            if node.next:
                msg += str(node.next.value) + " | "
            print(msg)
            node = node.next

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            self.size += 1
            return
        node = self.head
        while(node.next):
            node = node.next
        newNode = Node(value)
        node.next = newNode
        newNode.prev = node
        self.size += 1

    def pop(self):
        node = self.head
        while(node.next.next):
            node = node.next
        node.next = None
        self.size -= 1

    def appendFront(self, value):
        if self.head == None:
            self.append(value)
            return
        node = Node(value)
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1

    def popFront(self):
        if self.head == None:
            return
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1

    def linkListSize(self):
        return self.size

    def find(self, value):
        node = self.head
        pos = 0
        while(node):
            if node.value == value:
                return pos
            node = node.next
            pos += 1
        return -1

    def insertAfter(self, findValue, insertValue):
        pos = self.find(findValue)
        if self.head==None or pos==-1:
            self.append(insertValue)
            return
        node = self.head
        for i in range(pos):
            node = node.next
        nodeAfter = node.next
        nodeInsert = Node(insertValue)
        node.next = nodeInsert
        nodeInsert.prev = node
        nodeInsert.next = nodeAfter
    
    def deleteNode(self, value):
        pos = self.find(value)
        if self.head==None or pos==-1:
            return
        if pos==0 and self.size==1:
            self.pop()
            return
        node = self.head
        for i in range(pos):
            node = node.next
        nodePrev = node.prev
        nodeNext = node.next
        if nodePrev and nodeNext==None:
            self.pop()
        elif nodePrev==None and nodeNext:
            self.popFront()
        else:
            nodePrev.next = nodeNext
            nodeNext.prev = nodePrev

linkList = LinkList()
# Test append.
myChar = 'a'
for i in range(0, 5, 1):
    linkList.append(chr(ord(myChar) + i))
linkList.printLinkList("append")
# Test pop.
linkList.pop()
linkList.printLinkList("pop")
# Test appendFront.
linkList.appendFront('Z')
linkList.printLinkList("appendFront")
# Test popFront.
linkList.popFront()
linkList.printLinkList("popFront")
# Test linkListSize.
print("=== test linkListSize ===")
print(linkList.linkListSize())
# Test find.
print("=== test find ===")
print(linkList.find('c'))
# Test insertAfter.
linkList.insertAfter('c', 'Z')
linkList.printLinkList("insertAfter")
# Test deleteNode.
# linkList.deleteNode('z')
linkList.deleteNode('Z')
# linkList.deleteNode('a')
# linkList.deleteNode('d')
linkList.printLinkList("deleteNode")