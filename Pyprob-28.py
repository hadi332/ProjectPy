#Problem 28: Binary Search
#Implement a binary search algorithm to find the index of a given element in a sorted list.

def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    
    return -1

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_element = 2
index = binary_search(sorted_list, target_element)
if index != -1:
    print(f"Element {target_element} found at index {index}.")
else:
    print(f"Element {target_element} not found in the list.")
