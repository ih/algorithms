def maximizedXOR(L, R):
    max_xor = 0
    for i in range(L, R+1):
        for j in range(i, R+1):
            max_xor = i ^ j if i ^ j > max_xor else max_xor
    return max_xor

L = int(input())
R = int(input())
print maximizedXOR(L, R)
