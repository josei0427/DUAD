class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    head: Node

    def __init__(self, head):
        self.head = head

    def enqueue(self, new_node):
        current_node = self.head
        while (current_node.next is not None):
            print(current_node.data)
            current_node = current_node.next

        print(current_node.data)
        current_node.next = new_node

        print("Nuevo Ciclo")
        current_node = self.head
        while (current_node.next is not None):
            print(current_node.data)
            current_node = current_node.next

    def dequeue(self):
        self.head = self.head.next


first_node = Node("Hola mundo")
second_node = Node("Soy el segundo")
first_node.next = second_node

third_node =Node("Soy el tercero")
second_node.next = third_node


structure = Queue(first_node)

forth_node = Node("Soy el nuevo!")
structure.enqueue(forth_node)