class MinHeap:
    def __init__(self):
        self.array = []

    def insert(self, new_value):
        self.array.append(new_value)
        self.heapify(len(self.array)-1)

    def heapify(self, index):
        if index == 0:
            return
        else:
            parent_index = (index-1)/2
            if self.array[index] < self.array[parent_index]:
                self.array[index], self.array[parent_index] = self.array[parent_index], self.array[index]
                self.heapify(parent_index)

mh = MinHeap()

mh.insert(1)
mh.insert(4)
mh.insert(2)
mh.insert(3)
print mh.array
