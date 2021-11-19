# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

def bubble_sort(my_array):  # takes in an array [10,3,7,8,20,15,6]

    for i in range(len(my_array) - 1, 0, -1): #keeps track of the number of swaps. decreases after each loop
        for j in range(i): #loops through the list and swap elements
            if my_array[j] > my_array[j+1]: # if the current is greater than next
                temp = my_array[j]
                my_array[j] = my_array[j+1] #swap positions
                my_array[j+1] = temp

    return my_array

new_array = bubble_sort([64, 34, 25, 12, 22, 11, 90, 2])
print(new_array)