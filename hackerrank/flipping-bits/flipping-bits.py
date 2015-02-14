def flipNumber(number):
    bits = numberToBits(number, 32)
    flipped_bits = flipBits(bits)
    return bitsToNumber(flipped_bits)

def numberToBits(number, bit_length):
    bits = []
    while len(bits) < bit_length:
        bit = number % 2
        bits.insert(0, bit)
        number /= 2
    return bits

def flipBits(bits):
    return [1 if bit == 0 else 0 for bit in bits]

def bitsToNumber(bits):
    number = 0
    for i, bit in enumerate(bits[::-1]):
        number += bit * (2 ** i)
    return number


#print([flipNumber(i) for i in range(4)])
print flipNumber(2147483647)
print flipNumber(1)
print flipNumber(0)
