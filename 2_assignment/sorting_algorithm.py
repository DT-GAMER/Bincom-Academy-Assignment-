#!/usr/bin/python3

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place, no need to check them again
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Input the unsorted array from the user
unsorted_array = input("Enter the unsorted array (comma-separated numbers): ")
unsorted_array = [int(x) for x in unsorted_array.split(",")]

# Apply Bubble Sort to the array
bubble_sort(unsorted_array)

print("Sorted Array:", unsorted_array)

