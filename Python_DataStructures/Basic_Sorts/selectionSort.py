# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

def selection_sort(my_array): #takes in an array [10,3,7,8,20,15,21]

    #loop through to find min index
    for i in range(len(my_array)-1): #because we are keeping track ogf the index
        min_index = i

        #loop through the list starting from the unsorted list
        for j in range(i+1, len(my_array)): #starts at the next element on i but not include the len(arr) 
            if my_array[j] < my_array[min_index]:
                min_index = j
        if i != min_index: #if the current element is NOT where it is suppose to be 
            temp = my_array[i]
            my_array[i] = my_array[min_index]
            my_array[min_index] = temp

    return my_array

new_array = selection_sort([10,3,7,8,20,15,6])
print(new_array)