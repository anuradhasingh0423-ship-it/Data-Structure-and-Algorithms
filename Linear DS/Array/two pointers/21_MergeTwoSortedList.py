# 1. Define the Node structure LeetCode uses under the hood
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. Your LeetCode Solution Class
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        tail = dummy
        
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
            
        return dummy.next

# Helper function to print the linked list cleanly in the terminal
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("NULL")

# ========================================================
# 3. THE TEST DRIVER
# ========================================================
if __name__ == "__main__":
    # Construct List 1: 1 -> 2 -> 3 -> NULL
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)

    # Construct List 2: 1 -> 2 -> 4 -> NULL
    list2 = ListNode(1)
    list2.next = ListNode(2)
    list2.next.next = ListNode(4)

    # 4. Instantiate the object and run the solution
    solution = Solution()
    merged_head = solution.mergeTwoLists(list1, list2)

    # 5. Print the output
    print("-" * 40)
    print("Merged Linked List Output:")
    print_list(merged_head)
    print("-" * 40)