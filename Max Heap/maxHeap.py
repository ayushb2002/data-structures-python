class MaxHeap:
    def __init__(self, root):
        self.heap = [root]
        self.length = 1
        
    def insert(self, val):
        """
        Parent = floor(i/2)
        Left child = i*2
        Right child = i*2+1
        """
        self.heap.append(val)
        self.length += 1
        index = self.length - 1
        
        while True:
            p = index // 2
            parent = self.heap[p]
            if parent < val:
                temp = self.heap[p]
                self.heap[p] = self.heap[index]
                self.heap[index] = temp
                index = p
            else:
                break
    
    def delete(self):
        """Deletes the root node from the heap."""
        temp = self.heap[0]
        self.heap[0] = self.heap[self.length - 1]
        self.heap[self.length - 1] = temp
        self.heap.pop(self.length - 1)
        self.length -= 1
        i = 0
        while True:
            l, r = i*2, i*2+1 
            left, right = None, None
            if l<self.length:
                left = self.heap[l]
            if r<self.length:
                right = self.heap[r]
            
            if left is not None and right is not None:
                if left>right and left>self.heap[i]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[l]
                    self.heap[l] = temp
                    i = l
                elif right > left and right>self.heap[i]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[r]
                    self.heap[r] = temp
                    i = r
                else:
                    break
            elif left is not None and left > self.heap[i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[l]
                self.heap[l] = temp
                i = l
            elif right is not None and right > self.heap[i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[r]
                self.heap[r] = temp
                i = r
            else:
                break
    
    def printHeap(self):
        print(self.heap)

mh = MaxHeap(10)
mh.insert(20)
mh.insert(60)
mh.insert(30)
mh.insert(5)
mh.insert(50)
mh.insert(40)
mh.insert(20)

mh.printHeap()

mh.delete()
mh.printHeap()
mh.delete()
mh.printHeap()