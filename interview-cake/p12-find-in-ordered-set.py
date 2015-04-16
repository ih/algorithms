def binary_search(array, target):
    if len(array) == 1:
        return array[0] == target
    else:
        midpoint = len(array)/2
        if target < array[midpoint]:
            return binary_search(array[0:midpoint], target)
        elif target > array[midpoint]:
            return binary_search(array[midpoint:], target)
        else:
            assert target == array[midpoint]
            return True
