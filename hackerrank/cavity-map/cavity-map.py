import copy

input_map = []

file = open('failed-input06.txt')

for _ in range(int(file.readline())):
    row = file.readline()
    input_map.append([int(item) for item in str(int(row))])

def findCavities(ground_map):
    cavity_map =  copy.deepcopy(ground_map)
    for i in range(len(ground_map)):
        for j in range(len(ground_map)):
            if i == 0 or j == 0 or i == len(ground_map)-1 or j == len(ground_map)-1:
                cavity_map[i][j] = ground_map[i][j]
            elif isCavity(ground_map, i, j):
                cavity_map[i][j] = 'X'
            else:
                cavity_map[i][j] = ground_map[i][j]
    return cavity_map

def isCavity(ground_map, i, j):
    cell_value = ground_map[i][j]
    return ground_map[i-1][j] < cell_value and ground_map[i][j-1] < cell_value and ground_map[i+1][j] < cell_value and ground_map[i][j+1] < cell_value

def printMap(cell_map):
    for i in range(len(cell_map)):
        print ''.join([str(cell) for cell in cell_map[i]])

a = [[1, 1, 1, 2], [1, 9, 1, 2], [1, 8, 9, 2], [1, 2, 3, 4]]
printMap(findCavities(input_map))
#printMap(a)




