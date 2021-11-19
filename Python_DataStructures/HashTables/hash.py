# Hash tables are a type of data structure in which the address or the index value of the data element is generated from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value. In other words Hash table stores key-value pairs but the key is generated through a hashing function.

# Create a hash class
class HashTable:

    #initialize the class
    def __init__(self, size = 11):
        self.table_data = [None] * size #creates a table with 11 data and initializes each to None

    #create a hash function that calculates the address where each data should be stored using the key
    def hash_function(self, key):
        address = 0
        for i in key:
            address = (address + ord(i) * 23) % len(self.table_data) #returns an int from 0->size-1
        return address

    #create a print meethod to print the hash table
    def print_table(self):
        #loop through the table and print key value pairs
        for key, value in enumerate(self.table_data):
            print(key ,":", value)

    #create a method to set the value to a certain address
    def set_hash(self, key, value):
        location = self.hash_function(key) #get the location to set the value

        if self.table_data[location] == None: 
            self.table_data[location] = [] #initialize the address with an array
        self.table_data[location].append([key,value])

    #create a method to get the value
    def get_value(self,key):
        location = self.hash_function(key)  # get the location to set the value

        if self.table_data[location] is not None:
            for i in self.table_data[location]: #go to location and loop through the list
                if i[0] == key:
                    return i[1] #return the value

        return None

    #apppend all keys in an array to a list
    def add_key(self):
        key_list = [] #empty list to add keys

        for i in range(len(self.table_data)): #loop through the hash table
            if self.table_data[i] is not None: #if it contains data
                for j in self.table_data[i]: #loop through the data and get the key
                    key_list.append(j[0])

        return key_list


my_table = HashTable()

my_table.set_hash('George', 25)
my_table.set_hash('Jerry', 23)
my_table.set_hash('Badjessa', 24)
my_table.set_hash('Messi', 33)

my_table.print_table()

print(my_table.get_value('Badjessa'))

print(my_table.add_key())


