class Node:
    def __init__(self, data):
        self.data = data
        self.next = None               

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse_and_print(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")

# Taking Input
LL = LinkedList()
elements = int(input("Enter the number of elements to insert: "))
for _ in range(elements):
    n = int(input("Enter element: "))
    LL.insertAtEnd(n)

print("Original List:")
LL.traverse_and_print()
