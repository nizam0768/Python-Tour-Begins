# Node class
class Node:
    def __init__(self, data):
        self.data = data  # store data
        self.next = None  # pointer to next node

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # first node

    # Add node at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Print linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
