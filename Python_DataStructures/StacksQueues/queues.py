# A queue is a collection of objects that supports fast first-in, first-out (FIFO) semantics for inserts and deletes

#Create a node 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#Create your queue
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    #create a method to print the nodes in a queue
    def print_list(self):
        if self.length == 0:
            return False
        else:
            temp = self.first
            while temp is not None:
                print(temp.value)
                temp = temp.next

    #create a method to queue and enqueue it
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node #enqueue at the end
            self.last = new_node
        self.length += 1

    #create a method to dequeue and dequeue it 
    def dequeue(self):
        if self.length == 0:
            return None

        temp = self.first #dequeue from the front
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp.value




myQueue = Queue(5)
myQueue.enqueue("george")
myQueue.enqueue("vee")
myQueue.enqueue(10)
myQueue.enqueue(23)
myQueue.print_list()
print("-"*50)
print("value that was popped: " , myQueue.dequeue())
print("-"*50)
myQueue.print_list()