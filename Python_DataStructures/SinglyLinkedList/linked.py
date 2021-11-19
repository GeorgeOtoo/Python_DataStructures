# Create a Node 
class Node:
    def __init__(self, value): # each new node takes in value 

        self.value = value
        self.next = None # the next points to None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value) # create a new_node
        self.head = new_node # point the head pointer to the new node
        self.tail = new_node # point the tail pointer to the new node
        self.length = 1

    def print_list(self): #prints the elements in a linked list 
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value) #create a new node
        if self.head is None: #check if list is empty
            self.head = new_node #point both head and tail to new node 
            self.tail = new_node
        else:
            self.tail.next = new_node #append new node to the list
            self.tail = new_node
        self.length += 1 #increase the length

    def pop(self):
        if self.length == 0: #check if node is empty
            return None

        #Create two pointers and both points to head
        temp = self.head
        pre = self.head
        while temp.next is not None: #Loop through the link and move both pointers
            pre = temp
            temp = temp.next
        self.tail = pre #repoint tail to the node befpre the last
        self.tail.next = None #set the next for the new tail to none
        self.length -= 1 

        #if the length is ever 0 set head and tail to none
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp #return the Node that was popped


    def prepend(self, value):
        new_node = Node(value)  #create new node
        if self.length == 0: #check if list is empty
            self.head = new_node # if empty point head and tail to new_node
            self.tail = new_node
        else:
            new_node.next = self.head #if not, point new_node to self.head
            self.head = new_node #point the head to the new_node
        self.length += 1
        return True

    def pop_first(self): 
        if self.length == 0: #return 0 if the length is 0
            return None
        
        temp = self.head #create a temporary pointer to point to head
        self.head = self.head.next #move the head to the next node
        temp.next = None #pop first by setting next to none
        self.length -= 1

        if self.length == 0:
            self.tail = None #head is already point to None so tail must do same

        return temp

    def get_node(self, index): #get node from a list
        if index < 0 or index > self.length: #check if the index exists within range
            return None
        
        temp = self.head #create a temp variable and point it to head 
        for _ in range(index): #Loop to go through the Linked List
            temp = temp.next #Move temp after each iteration
        return temp #return the value of last positon of temp {A node} 

    def set_value(self, index, value):  # set node in a list
        temp = self.get_node(index) #call the get method to return the position of temp {a Node}

        if temp is not None: #if temp is not none, set the value of temp to value
            temp.value = value
            return True
        return False #if not return true

    def insert(self, index, value):
        new_node = Node(value) #create a new node

        #check if index is out of range
        if index < 0 or index > self.length:  # check if the index exists within range
            return False
        
        #check if index is 0
        if index == 0:
            return self.prepend(value)

        #check if index is the length of the list
        if index == self.length:
            return self.append(value)
        
        #insert at a particular node with a given index
        temp = self.get_node(index-1) #call the get function to get the position of the node
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True


    def remove(self, index): 

        #check if index is out of range
        if index < 0 or index > self.length:  # check if the index exists within range
            return None

        #check if index is 0
        if index == 0:
            return self.pop_first()

        #check if index is the length of the list
        if index == self.length-1:
            return self.pop()

        #insert at a particular node with a given index
        prev = self.get_node(index-1) #call the get function to get the position of the node
        temp = prev.next #points to the node next to prev
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail #switch head and tail
        self.tail = temp

        before = None #tracker to track before temp
        after = temp.next  # tracker to track before temp
        
        for _ in range(self.length): #Loop to loop through the ll and reverse it
            after = temp.next 
            temp.next = before
            before = temp
            temp = after

myLink = LinkedList(4)
myLink.append(5)
myLink.append(8)
myLink.append(11)

myLink.print_list()
print(myLink.pop())
myLink.prepend(100)
myLink.print_list()
print(myLink.pop_first())
print("-"*50)
print(myLink.get_node(2))
myLink.set_value(2, 1013)
print("-"*50)
myLink.insert(2,2001)

print("-"*50)
myLink.remove(3)
myLink.print_list()

print("-"*50)
myLink.reverse()
myLink.print_list()





    #def append(self, value):
    #def prepend (self, value):
    #def insert(self, value):
