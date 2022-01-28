class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self, ):
        if self.top is None:
            return None
        topNode = self.top.item
        self.top=self.top.next
        return topNode.item

    def is_empty(self):
        return self.top is None