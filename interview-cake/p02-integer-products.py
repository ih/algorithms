def products(array):
    # handle case array size 1
    solution = []
    for index in range(0, len(array)):
        if index == 0:
            solution.append(1)
        else:
            solution.append(array[index-1]*solution[index-1])

    after_product = 1
    for index in reversed(range(0, len(array))):
        if index != len(array) - 1:
            after_product = after_product * array[index+1]
        solution[index] = after_product * solution[index]
    return solution

print products([1, 2, 6, 5, 9])
