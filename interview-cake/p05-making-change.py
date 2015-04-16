# recursive/memoized
def make_change(amount, denominations):
    if len(denominations) == 1:
        return 1 if amount % denominations[0] == 0 else 0
    if amount < 0:
        return 0
    elif amount == 0:
        return 1
    else:
        total = 0
        for index, denomination in enumerate(denominations):
            amount_left = amount
            while amount_left > -1:
                amount_left -= denomination
                total += make_change(amount_left, denominations[index+1:])
        return total

print make_change(4, [1, 2, 3])

print make_change(2, [1, 2])

print make_change(10, [2, 5, 3, 6])

print 'make_change2'

# dynamic programming
def make_change2(amount, denominations):
    number_of_ways = [1 if i % denominations[0] == 0 else 0
                      for i in range(amount+1)]
    if len(denominations) == 1:
        return number_of_ways[-1]
    for denomination in denominations[1:]:
        for index, ways in enumerate(number_of_ways):
            if (index)-denomination >= 0:
                number_of_ways[index] = (
                    number_of_ways[index] + number_of_ways[(index)-denomination])
    return number_of_ways[-1]


print make_change2(2, [1, 2])
print make_change2(4, [1, 2, 3])
print make_change2(10, [2, 3, 5, 6])
