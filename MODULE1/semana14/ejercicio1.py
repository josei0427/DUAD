class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def pop(self):
        if self.head is None:
            return None
        remove_node = self.head.data
        self.head = self.head.next
        return remove_node


    def print_stack(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next



stack = Stack()
stack.push("Joey")
stack.push("Chandler")
stack.push("Ross")

stack.print_stack()
print()
stack.pop()
stack.print_stack()