# Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part

def insertion_sort(my_array):  # takes in an array [10,3,7,1,20,15,21]

    for i in range(1, len(my_array)):
        temp = my_array[i]
        j = i - 1


        while temp < my_array[j] and j > -1:
            my_array[j+1] = my_array[j]
            my_array[j] = temp
            j -= 1

    return my_array


new_array = insertion_sort([10, 3, 7, 1, 20, 15, 21]) #3,7,1,10,15,20,21
print(new_array)

