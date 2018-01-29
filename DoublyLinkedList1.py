#Paired Programming by 59112019 & 74412019
# A class to represent a node in a doubly-linked list
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.prev = None
        self.next = None

    def getData(self):
        return self.data

    def getPrev(self):
        return self.prev

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setPrev(self, newprev):
        self.prev = newprev
        
    def setNext(self,newnext):
        self.next = newnext

# A class to represent a doubly-linked list
class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.n_nodes = 0

    def isEmpty(self):
        return self.head == None

    # Add an item to the beginning of the list
    def addFirst(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        if (temp.getNext() != None):
            temp.getNext().setPrev(temp)
        self.head = temp

        # if this was the first node added, self.tail should
        # also point to it
        if (self.tail == None):
            self.tail = temp
            
        self.n_nodes = self.n_nodes + 1

    # Add an item to the end of the list
    def addLast(self,item):
        temp = Node(item)
        temp.setPrev(self.tail)
        if (temp.getPrev() != None):
            temp.getPrev().setNext(temp)
        self.tail = temp

        # if this was the first node added, self.head should
        # also point to it
        if (self.head == None):
            self.head = temp
            
        self.n_nodes = self.n_nodes + 1

    # Return the size of the list
    def size(self):
        return self.n_nodes


    # Removes the first item in the list
    def removeFirst(self):
        # if the list has two or more elements, remove the first one
        if (self.head != self.tail):
            itemToRemove = self.head
            self.head = itemToRemove.getNext()
            self.head.setPrev(None)

        # if the list has one element, we should make it empty
        elif(self.head != None):
            self.head = None
            self.tail = None
            
        self.n_nodes = self.n_nodes -1

    # Removes the last item in the list
    def removeLast(self):
        # if the list has two or more elements, remove the last one
        if (self.head != self.tail):
            itemToRemove = self.tail
            self.tail = itemToRemove.getPrev()
            self.tail.setNext(None)

        # if the list has one element, we should make it empty
        elif(self.head != None):
            self.head = None
            self.tail = None
            
        self.n_nodes = self.n_nodes -1

    # A method to print the list
    def printList(self):
        if (self.head == None):
            print("EMPTY LIST")
        else:
            current = self.head
            while current.getNext() != None:
                print(current.getData(), end=" <-> ")
                current = current.getNext()
            print(current.getData())

    # A method to print the list in reverse order
    def printListBackwards(self):
        if (self.tail == None):
            print("EMPTY LIST")
        else:
            current = self.tail
            while current.getPrev() != None:
                print(current.getData(), end=" <-> ")
                current = current.getPrev()
            print(current.getData())

    def insert(self, pos, item):
        new=Node(item)
        current = self.head
        count = 0
        previous = None
        stop =False
        while current != None and not stop:
            if count==(pos):
                stop = True
            else:
                previous= current
                current = current.getNext()
            count = count + 1
        if previous == None:
            self.head = new
        else:
            new.setNext(current)
            previous.setNext(new)

        
# Test code
mylist = DoublyLinkedList()

mylist.addFirst(31)
print("Added first: ", end="")
mylist.printList()

mylist.addLast(77)
print("Added last: ", end="")
mylist.printList()

mylist.addFirst(17)
print("Added first: ", end="")
mylist.printList()

mylist.addFirst(93)
print("Added first: ", end="")
mylist.printList()

mylist.addFirst(26)
print("Added first: ", end="")
mylist.printList()

mylist.addFirst(54)
print("Added first: ", end="")
mylist.printList()

print("The list's size is:",mylist.size())

print("Removing first: ", end="")
mylist.removeFirst()
mylist.printList()

print("Removing last: ", end="")
mylist.removeLast()
mylist.printList()

print("Removing last: ", end="")
mylist.removeLast()
mylist.printList()

print("The list in reverse order is: ", end="")
mylist.printListBackwards()

b = mylist.insert(2, '500')
print(b)

