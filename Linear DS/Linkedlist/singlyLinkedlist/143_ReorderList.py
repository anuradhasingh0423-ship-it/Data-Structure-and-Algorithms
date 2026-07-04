# 1. Define the Node structure LeetCode uses under the hood
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. Your LeetCode Solution Class
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Phase 1: Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Phase 2: Reverse second half
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # Phase 3: Zipper Merge
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

# ========================================================
# 3. THE TEST DRIVER (Add this to run locally)
# ========================================================
def print_list(head):
    """Helper function to print our linked list cleanly"""
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("NULL")

if __name__ == "__main__":
    # Create the nodes for Example 1: [1, 2, 3, 4, 5]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original List:")
    print_list(head)
    print("-" * 30)

    # Instantiate your solution class and call the function
    sol = Solution()
    sol.reorderList(head)

    print("Reordered List Output:")
    print_list(head)