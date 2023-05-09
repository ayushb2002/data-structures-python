def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    breakPoint = len(arr) // 2
    left = mergeSort(arr[:breakPoint])
    right = mergeSort(arr[breakPoint:])
    
    return mergeSortUtil(left, right)

def mergeSortUtil(left, right):
    leftPtr, rightPtr = 0, 0
    arr = []
    while leftPtr < len(left) and rightPtr < len(right):
        if left[leftPtr] < right[rightPtr]:
            arr.append(left[leftPtr])
            leftPtr += 1
        elif left[leftPtr] > right[rightPtr]:
            arr.append(right[rightPtr])
            rightPtr += 1
        else:
            arr.append(left[rightPtr])
            arr.append(right[rightPtr])
            leftPtr += 1
            rightPtr += 1
            
    while leftPtr < len(left):
        arr.append(left[leftPtr])
        leftPtr += 1
        
    while rightPtr < len(right):
        arr.append(right[rightPtr])
        rightPtr += 1
        
    return arr

arr = [6, 5, 10, 12, 9, 1, 0]

print(mergeSort(arr))