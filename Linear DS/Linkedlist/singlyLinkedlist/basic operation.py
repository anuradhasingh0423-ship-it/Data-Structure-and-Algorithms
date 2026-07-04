class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # 1. ADD FIRST - O(1)
    def add_first(self, data):
        new_node = Node(data)
        self.size += 1
        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

    # 2. ADD LAST - O(1) because we keep a tail pointer
    def add_last(self, data):
        new_node = Node(data)
        self.size += 1
        if self.head is None:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    # 3. PRINT LINKED LIST - O(n)
    def print_linked_list(self):
        if self.head is None:
            print("LL is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # 4. ADD AT INDEX - O(n)
    def add(self, idx, data):
        if idx == 0:
            self.add_first(data)
            return
        
        new_node = Node(data)
        self.size += 1
        temp = self.head
        i = 0
        while i < idx - 1:
            temp = temp.next
            i += 1

        new_node.next = temp.next
        temp.next = new_node

    # 5. REMOVE FIRST - O(1)
    def remove_first(self):
        if self.size == 0:
            print("LL is empty")
            return float('-inf')  # Equivalent to Integer.MIN_VALUE
        elif self.size == 1:
            val = self.head.data
            self.head = self.tail = None
            self.size = 0
            return val

        val = self.head.data
        self.head = self.head.next
        self.size -= 1
        return val

    # 6. REMOVE LAST - O(n)
    def remove_last(self):
        if self.size == 0:
            print("LL is empty")
            return float('-inf')
        elif self.size == 1:
            val = self.head.data
            self.head = self.tail = None
            self.size = 0
            return val

        prev = self.head
        for _ in range(self.size - 2):
            prev = prev.next

        val = self.tail.data
        prev.next = None
        self.tail = prev
        self.size -= 1
        return val

    # 7. RECURSIVE SEARCH - O(n) time, O(n) call stack space
    def _helper(self, node, key):
        if node is None:
            return -1
        if node.data == key:
            return 0

        idx = self._helper(node.next, key)
        if idx == -1:
            return -1
        return idx + 1

    def rec_search(self, key):
        return self._helper(self.head, key)

    # 8. IN-PLACE REVERSAL - O(n) time, O(1) space
    def reverse(self):
        prev = None
        curr = self.tail = self.head
        
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    # 9. DELETE N-TH NODE FROM END - O(n)
    def delete_nth_node(self, n):
        sz = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            sz += 1

        if n == sz:
            self.head = self.head.next
            return

        i = 1
        i_to_find = sz - n
        prev = self.head
        while i < i_to_find:
            prev = prev.next
            i += 1

        prev.next = prev.next.next

    # 10. FIND MIDPOINT (Tortoise & Hare variant)
    def _find_mid_node(self, head):
        slow = head
        fast = head
        # Note: Your Java loop uses `fast != null && fast.next != null`. 
        # For a true palindrome mid-split, this stops at the exact center.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 11. CHECK PALINDROME - O(n) time, O(1) space
    def check_palindrome(self):
        if self.head is None or self.head.next is None:
            return True

        # Step A: Find midpoint
        mid_node = self._find_mid_node(self.head)

        # Step B: Reverse second half
        curr = mid_node
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step C: Compare Left and Right halves
        right = prev
        left = self.head
        while right is not None:
            if left.data != right.data:
                return False
            right = right.next
            left = left.next
        return True


# ==========================================
#               TEST DRIVE
# ==========================================
if __name__ == "__main__":
    ll = LinkedList()
    
    ll.add_first(2)
    ll.add_first(1)
    ll.add_last(2)
    ll.add_last(1)  # Modified from 3 to 1 to test True palindrome case [1, 2, 2, 1]

    print("Linked List:")
    ll.print_linked_list()  # Output: 1 2 2 1
    
    print("Is Palindrome?:", ll.check_palindrome())  # Output: True