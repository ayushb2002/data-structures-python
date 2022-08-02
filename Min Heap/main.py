import sys


class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize+1)
        self.Heap[0] = -1*sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos//2

    def leftChild(self, pos):
        return 2*pos

    def rightChild(self, pos):
        return (2*pos) + 1

    def isLeaf(self, pos):
        return pos*2 > self.size

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            smallest = pos
            rightPos = self.rightChild(pos)
            leftPos = self.leftChild(pos)

            if self.Heap[leftPos] < self.Heap[pos]:
                smallest = leftPos

            if self.Heap[rightPos] < self.Heap[pos]:
                smallest = rightPos

            self.swap(pos, smallest)

    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)

    def insert(self, element):
        if self.size >= self.maxsize:
            return

        self.size += 1
        self.Heap[self.size] = element

        current = self.size
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def printHeap(self):
        for i in range(1, (self.size//2)+1):
            print(
                f" Parent: {self.Heap[i]} Left Child: {self.Heap[2*i]} Right Child: {self.Heap[2*i+1]}")

    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped


if __name__ == "__main__":
    print('Initial minHeap: ')
    minHeap = MinHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.minHeap()

    minHeap.printHeap()
    print("The Min val is " + str(minHeap.remove()))
    print("Updated minHeap: ")
    minHeap.minHeap()
    minHeap.printHeap()
