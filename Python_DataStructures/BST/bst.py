# A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties.The left sub-tree of a node has a key less than or equal to its parent node's key.The right sub-tree of a node has a key greater than to its parent node's key.

# create a node class with right and left pointers
class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

# create a class for the tree search
class Tree:
    def __init__(self,value):
        new_node = Node(value)
        self.root = new_node
    
    #create a method to insert nodes to the tree
    def insert(self, value):
        new_node = Node(value) # create a new node and when BST is empty assign root to new node
        if self.root == None:
            self.root = new_node
            return True

        temp = self.root
        while(True): #create a while loop to loop through the search tree and insert the node

            if new_node.value == temp.value: #if new node and temp have the same value in the tree
                return False

            if new_node.value < temp.value: #check if new_node is less than the temp value
                if temp.left == None: #if yes and the temp.left value is none
                    temp.left = new_node #set the left to new node  
                    return True
                temp = temp.left #move on to the next node and start from the begining if not
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    # create a method that searches the tree and sees if a value is in the tree
    def contains(self, value):

        if self.root == None: #if the tree is empty
            return False

        temp = self.root
        while temp is not None: 
            if value < temp.value: #if the value is less move temp and start over
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                if value == temp.value:
                    return True
        return False #return false if the value doesn't exist  

myTree = Tree(10)
print(myTree.root.value)
myTree.insert(6)
myTree.insert(15)
myTree.insert(20)
myTree.insert(8)
myTree.insert(1)
#print(myTree.root.left.value)
#print(myTree.root.left.value)
#print(myTree.root.right.value)

print(myTree.contains(100))

        


        