def findHighestProduct(array_of_ints):
    lowest = min(array_of_ints[:3])
    second_lowest = findNext(array_of_ints[:3], [lowest], min)
    highest = max(array_of_ints[:3])
    second_highest = findNext(array_of_ints[:3], [highest], max)
    third_highest = findNext(array_of_ints[:3], [highest, second_highest], max)

    if len(array_of_ints) <= 3:
        return reduce(lambda x, y: x*y, array_of_ints)
    else:
        for integer in array_of_ints[3:]:
            if integer <= lowest:
                second_lowest = lowest
                lowest = integer
            if integer > lowest and integer < second_lowest:
                second_lowest = integer
            if integer >= highest:
                third_highest = second_highest
                second_highest = highest
                highest = integer
            if integer < highest and integer >= second_highest:
                third_highest = second_highest
                second_highest = integer
            if (integer < highest and integer < second_highest
                    and integer > third_highest):
                third_highest = integer
        return max(
            third_highest*second_highest*highest, highest*lowest*second_lowest)


def findNext(array, elements, function):
    [array.remove(element) for element in elements]
    return function(array)

print findHighestProduct([1, 2, 3])
print findHighestProduct([1, 2, 3, -1, 4])
print findHighestProduct([1, 10, -5, 1, -100])
