class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Every new node initially points to nothing

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # The list starts completely empty
     
    # --- DELETE OPERATION ---
    def delete(self, val):
        temp = self.head
        
        # Guard 1: If the list is completely empty, do nothing
        if temp is None:
            print("The list is empty!")
            return
            
        # Guard 2: If the HEAD node itself holds the target value
        if temp.data == val:  
            self.head = temp.next
            return

        # Scenario 3: The target is deeper inside the list
        prev = None
        found = False
        
        while temp is not None:
            if temp.data == val:
                found = True
                break
            prev = temp 
            temp = temp.next
            
        # If we broke out of the loop because we found it, adjust pointers
        if found:
            prev.next = temp.next
        else:
            print(f"Node with value {val} not found.")    

    # --- TRAVERSE OPERATION ---
    def traverse(self):
        current = self.head
        
        # Guard: Checking if there's anything to print
        if current is None:
            print("Empty List: NULL")
            return
            
        # Walk through each node until we hit the end (None)
        while current:
            print(current.data, end=" -> ")
            current = current.next  # Jump to the next memory node
            
        print("NULL")


# --- Verification Test Drive ---
if __name__ == "__main__":
    ll = SinglyLinkedList()
    


    print("\n--- Step 2: Deleting a middle element (20) ---")
    ll.delete(20)
    ll.traverse()        # Output: 10 -> 30 -> NULL

    print("\n--- Step 3: Deleting the head element (10) ---")
    ll.delete(10)
    ll.traverse()        # Output: 30 -> NULL

    print("\n--- Step 4: Deleting a non-existent element (99) ---")
    ll.delete(99)        # Output: Node with value 99 not found.