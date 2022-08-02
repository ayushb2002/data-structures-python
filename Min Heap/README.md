### A Min Heap is a Complete Binary Tree. A Min heap is typically represented as an array. The root element will be at Arr[0]. For any ith node, i.e., Arr[i]:

- Arr[(i -1) / 2] returns its parent node.
- Arr[(2 * i) + 1] returns its left child node.
- Arr[(2 * i) + 2] returns its right child node.

#### Operations on Min Heap :

- getMin(): It returns the root element of Min Heap. Time Complexity of this operation is O(1).
- extractMin(): Removes the minimum element from MinHeap. Time Complexity of this Operation is O(Log n) as this operation needs to maintain the heap property (by calling heapify()) after removing root.
- insert(): Inserting a new key takes O(Log n) time. We add a new key at the end of the tree. If new key is larger than its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.
