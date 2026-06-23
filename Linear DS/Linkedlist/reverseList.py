def reverseList(self, head):
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next  # 1. Save the next node's address
        curr.next = prev       # 2. Reverse the arrow to point backward
        prev = curr            # 3. Move 'prev' one step forward
        curr = next_node       # 4. Move 'curr' one step forward
        
    return prev  # 'prev' ends up pointing to the brand new head node
