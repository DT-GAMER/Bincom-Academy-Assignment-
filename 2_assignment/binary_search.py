#!/usr/bin/python3

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Input the sorted array from the user
sorted_array = input("Enter the sorted array (comma-separated numbers): ")
sorted_array = [int(x) for x in sorted_array.split(",")]

# Input the target value from the user
target_value = int(input("Enter the target value to search for: "))

# Perform binary search on the sorted array for the target value
index = binary_search(sorted_array, target_value)

# Check if the target value was found
if index != -1:
    print(f"Found {target_value} at index {index}.")
else:
    print(f"{target_value} not found in the array.")

