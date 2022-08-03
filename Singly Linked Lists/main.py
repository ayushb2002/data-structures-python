class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = newNode

        return True

    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        return True

    def insertAfter(self, after, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            node = self.search(after)
            if not node:
                return False

            ptr = node.next
            node.next = newNode
            newNode.next = ptr

        return True

    def search(self, element):
        ptr = self.head
        while ptr.next != None:
            if ptr.data == element:
                return ptr
            else:
                ptr = ptr.next

        return None

    def printLL(self):
        ptr = self.head
        if not ptr:
            return
        while ptr != None:
            print(ptr.data, end=" ")
            ptr = ptr.next

        print()

    def deleteNode(self, data):
        ptr = self.head
        if ptr.data == data:
            self.head = ptr.next
            return True
        while ptr != None:
            if ptr.next == None:
                return False
            if ptr.next.data == data:
                break
            ptr = ptr.next

        if not ptr:
            return False

        nxt = ptr.next
        ptr.next = nxt.next
        return True


if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtBeginning(10)
    ll.insertAtEnd(20)
    ll.insertAtEnd(30)
    ll.insertAtEnd(50)
    ll.insertAtBeginning(0)
    ll.insertAfter(30, 40)
    ll.printLL()
    ll.deleteNode(0)
    ll.printLL()
