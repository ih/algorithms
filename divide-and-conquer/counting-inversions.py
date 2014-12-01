# brute force
import random

def brute_inversions(input_array):
    inversions = 0
    for i,element in enumerate(input_array):
        for j, later_element in enumerate(input_array[i:]):
            if element > later_element:
                inversions += 1
    return inversions

print brute_inversions([1, 2, 3, 4, 5])
print brute_inversions([1, 3, 5, 2, 4, 6])

def count_inversions(input_array):
    return sort_and_count_inversions(input_array)[0]

def sort_and_count_inversions(input_array):
    if len(input_array) == 1:
        return 0, input_array
    else:
        pivot = len(input_array) / 2
        left_array = input_array[:pivot]
        right_array = input_array[pivot:]
        left_inversions, sorted_left = sort_and_count_inversions(left_array)
        right_inversions, sorted_right= sort_and_count_inversions(right_array)
        cross_inversions, sorted_array= merge_cross_inversions(sorted_left, sorted_right)
        return (left_inversions + right_inversions + cross_inversions, sorted_array)

def merge_cross_inversions(left_array, right_array):
    inversions = 0
    sorted_array = []
    while len(left_array) > 0 and len(right_array) > 0:
        if left_array[0] <= right_array[0]:
            sorted_array.append(left_array.pop(0))
        else:
            inversions += len(left_array)
            sorted_array.append(right_array.pop(0))
    remaining = left_array if len(right_array) == 0 else right_array
    return (inversions, sorted_array + remaining)

print count_inversions([1, 2, 3, 4, 5])
print count_inversions([1, 3, 5, 2, 4, 6])


random_array = [random.randint(0, 100) for i in range(100)]

print brute_inversions(random_array)
print count_inversions(random_array)
