class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Every new node initially points to nothing

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # The list starts completely empty

    # --- APPEND OPERATION ---
    def append(self, data):
        new_node = Node(data)
        
        # Case 1: The list is empty, make this the head
        if not self.head:
            self.head = new_node
            return
            
        # Case 2: Walk to the end of the list
        current = self.head
        while current.next:  # Stop when current.next is None (the last node)
            current = current.next
            
        # Link the old tail node to our new node
        current.next = new_node

    # --- TRAVERSE OPERATION ---
    def traverse(self):
        current = self.head
        
        # Walk through each node until we hit the end (None)
        while current:
            print(current.data, end=" -> ")
            current = current.next  # Jump to the next memory node
            
        print("NULL")

# --- Testing the Code ---
ll = SinglyLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.traverse()  # Output: 10 -> 20 -> 30 -> NULL









