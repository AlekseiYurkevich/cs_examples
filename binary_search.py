def binarySearch(array, target):
    # Write your code here.
    return binary_search_helper(array, target, 0, len(array) - 1)


def binary_search_helper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potential_match = array[middle]
    if target == potential_match:
        return middle
    elif target < potential_match:
        return binary_search_helper(array, target, left, middle - 1)
    else:
        return binary_search_helper(array, target, middle + 1, right)
	