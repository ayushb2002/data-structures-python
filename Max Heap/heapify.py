def heapifyUtil(arr, n, i):
    """
    Runs backwards on an array skipping the leaf nodes (floor(n/2)). Takes time of O(log n).
    """
    largest = i
    l = 2*i # left child
    r = 2*i+1 # right child
    
    if l<n and arr[l] > arr[largest]:
        largest = l
    if r<n and arr[r] > arr[largest]:
        largest = r
        
    if largest != i:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp

        heapifyUtil(arr, n, largest) # to maintain heap ordering after 
        
    return arr
        
def buildHeap(arr):
    """
    This is an O(n) algorithm for generating heap.
    """
    n = len(arr)
    for i in range(n//2, -1, -1):
        arr = heapifyUtil(arr, n, i)
        
    return arr

arr = [40, 10, 30, 50, 60, 15]
print(buildHeap(arr))