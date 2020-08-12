# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    middle = (start +end)//2 # divide by 2 and get middle

    if len(arr) == 0:
        return -1

    # if target is equal to the middle index: return middle
    if arr[middle] == target:
        return middle

    # if target is less than middle: left turn clyde
    elif arr[middle] > target:
        return binary_search(arr, target, end, middle -1)

    # if target is greater than the middle: right turn clyde
    else:
        return binary_search(arr, target, start, middle + 1)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
#def agnostic_binary_search(arr, target):
    # Your code here

