# Create a Node class
class Node:
    def __init__(self, value): # a constructor to initialize
        self.value = value
        self.next = None
        self.prev = None

#Create the Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value) #create new node
        self.head = new_node
        self.tail = new_node
        self.length = 1

    #create method to append nodes to the list
    def append(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    #create a method to loop through the entire list
    def print_list(self):
        if self.length == 0:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #create a method to add a node to the beginnig of a ll
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            temp.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    #create a method to pop nodes from a list
    def pop(self):
        if self.length == 0: #if there are no nodes in the ll
            return None

        temp = self.tail

        if self.length == 1: #if there is only one node in the LL
            self.head = None
            self.tail = None
        else:                #if there are two or more nodes in the LL
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None 
        self.length -= 1
        return temp


    #create method to pop the first node in the LL
    def pop_first(self):
        if self.length == 0: #if there are no nodes in the ll
            return None

        temp = self.head

        if self.length == 1: #if there is only one node in the LL
            self.head = None
            self.tail = None
        else:
            self.head = temp.next 
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    #create a method to get a node at a specific index
    def get_node(self, index):
        if self.length == 0:  # if there are no nodes in the ll
            return None
        if index < 0 or index >= self.length: #check if index is out of bound
            return None

        temp = self.head #assign temp to head

        if index < self.length/2: #check if index is at the first half
            for _ in range(index): #loop through if it is at the first half
                temp = temp.next
        else:
            temp = self.tail #assign temp to tail
            for _ in range(self.length-1, index, -1): #loop from the back if it is
                temp = temp.prev

        return temp


    #create a method to set the value of a node in a DLL
    def set_node(self, index, value):
        if index < 0 or index > self.length: #check if index is out of bound 
            return None
            
        temp = self.get_node(index)
        if temp is not None:
            temp.value = value
            return True

        return False

    #create a method to insert a node to a Dll
    def insert(self, index, value):
        new_node = Node(value)

        if index < 0 or index > self.length:
            return False

        if self.length == 0: #if the list is empty set head and tail to point to node
            self.head = new_node
            self.tail = new_node

        if index == 0: #if index is 0 call the prepend method
            return self.prepend(value)

        if index == self.length: #if index is at the end DLL call append method
            return self.append(value)

        before = self.get_node(index-1)
        after = before.next
        before.next = new_node
        new_node.prev = before
        new_node.next = after
        after.prev = new_node
        self.length += 1
        return True

    #create method to remove a node from a list
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length-1:
            return self.pop()

        temp = self.get_node(index)
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None

        self.length -= 1

        return temp





#create your DLL
myList = DoublyLinkedList(8)
myList.append(12)
myList.append(100)
myList.append(7)
myList.prepend(56)
myList.print_list()
print("-"*50)
print(myList.pop_first())
print("-"*50)
myList.print_list()
print("-"*50)
print(myList.get_node(2))
print(myList.get_node(3))
print("-"*50)
myList.set_node(3,999)
myList.print_list()
print("-"*50)
myList.insert(3,777)
myList.print_list()
print("-"*50)
print(myList.remove(2))
print("-"*50)
myList.print_list()
