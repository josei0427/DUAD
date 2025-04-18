class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_number(self, value):
        if self.value is None:
            self.value = value
        elif value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.add_number(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.add_number(value)

    def print_tree(self):
        if not self:
            return
        queue = [self]
        while queue:
            node = queue.pop(0)
            print(node.value, end=" ")
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


nums = [10, 5, 15, 6, 8, 12, 3, 7, 18, 2]

root = Node(None)

for value in nums:
    root.add_number(value)

root.print_tree()