class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DQueue:
    head: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return data

    def pop_right(self):
        if self.tail is None:
            return None
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return data

    def print_de_queue(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()


de_queue = DQueue()
de_queue.push_left("Monica")
de_queue.push_right("Rachel")
de_queue.push_left("Pheobe")
de_queue.print_de_queue()
de_queue.pop_left()
de_queue.print_de_queue()
de_queue.pop_right()
de_queue.print_de_queue()