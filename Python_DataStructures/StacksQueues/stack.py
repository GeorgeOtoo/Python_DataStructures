# A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.

# create a node constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# create a stack class


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    # create a print method to print the nodes in a stack
    def print_list(self):
        if self.top == None:
            return False

        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # create a method to push nodes into a stack
    def push(self, value):
        new_node = Node(value)

        # check if stack is empty
        if self.height == 0:
            self.top = new_node
        else:  # push the new node into the stack
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    # create a method to pop nodes from the stack
    def pop(self):
        if self.height == 0:  # check if the stack is empty
            return None

        temp = self.top  # if not remove the node at the top
        self.top = temp.next
        temp.next = None
        self.height -= 1

        return temp.value


myStack = Stack(6)
myStack.push(10)
myStack.push(117)
myStack.push(223)
myStack.print_list()

print("-"*50)
print(myStack.pop())

print("-"*50)
print("-"*50)
myStack.print_list()


