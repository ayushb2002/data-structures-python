class Stack:
    def __init__(self):
        self.stack = []
        self.topEl = None

    def push(self, item):
        self.stack.insert(0, item)
        self.topEl = self.stack[0]
        return self.topEl

    def pop(self):
        popped = self.stack[0]
        self.stack.pop(0)
        return popped

    def top(self):
        return self.topEl

    def empty(self):
        if self.stack == []:
            return True
        else:
            return False

    def size(self):
        return len(self.stack)

    def printStack(self):
        print(self.stack)


if __name__ == "__main__":
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    print("Initial Stack: ")
    st.printStack()

    st.pop()
    print("Stack after first pop!")
    st.printStack()
    st.pop()
    print("Stack after second pop!")
    st.printStack()
