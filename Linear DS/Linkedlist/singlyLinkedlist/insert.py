class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    # --- INSERT OPERATION ---
    def insert_at(self, val, position):
        new_node = Node(val)
        
        # Scenario A: Inserting at the very front (Index 0)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return  # Exit early since we are done
            
        # Scenario B: Inserting in the middle or end
        current = self.head
        prev_node = None
        count = 0
        
        # Traverse until we reach the target index OR hit the end of the list
        while current is not None and count < position:
            prev_node = current
            current = current.next
            count += 1
            
        # Safety Check: If position is completely out of bounds
        if prev_node is None:
            print("Position out of bounds!")
            return

        # Stitch the new node into the gap
        prev_node.next = new_node
        new_node.next = current        

    # --- TRAVERSE OPERATION ---
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next  
        print("NULL")

# --- Testing the Code ---
ll = SinglyLinkedList()
ll.insert_at(10, 0)  # Fixed method name and parameter order (val=10, position=0)
ll.insert_at(30, 1)  # Append 30 at index 1
ll.insert_at(20, 1)  # Insert 20 at index 1 (between 10 and 30)

ll.traverse()  # Expected Output: 10 -> 20 -> 30 -> NULL