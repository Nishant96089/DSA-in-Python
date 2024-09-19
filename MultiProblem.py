class Node:
    def __init__(self, data):  # Correcting the __init__ method
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):  # Correcting the __init__ method
        self.head = None
    
    def insertAtHead(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def traverse_and_print(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")
    
    def search(self, k):
        temp = self.head
        while temp:
            if temp.data == k:
                return True
            temp = temp.next
        return False
    
    def sort_ascending(self):
        if self.head is None:
            return
        
        sorted_list = None
        current = self.head
        
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        
        self.head = sorted_list
    
    def sorted_insert(self, head, node):
        if head is None or head.data >= node.data:
            node.next = head
            return node
        else:
            current = head
            while current.next and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
        return head
    
    def sort_descending(self):
        self.sort_ascending()
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Taking input from the user
LL = LinkedList()
num_elements = int(input("Enter the number of elements to insert: "))
for _ in range(num_elements):
    element = int(input("Enter element: "))
    LL.insertAtHead(element)

print("Original List:")
LL.traverse_and_print()

print("Sorted List (Ascending):")
LL.sort_ascending()
LL.traverse_and_print()

print("Sorted List (Descending):")
LL.sort_descending()
LL.traverse_and_print()

search_key = int(input("Enter a number to search: "))
print(f"Search for {search_key}: {'Found' if LL.search(search_key) else 'Not Found'}")