class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("NULL")

if __name__ == "__main__":
    # Create list: 1 -> 1 -> 2 -> 3 -> 3 -> NULL
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)

    print("Original Linked List:")
    print_list(head)
    print("-" * 30)

    solution = Solution()
    cleaned_head = solution.deleteDuplicates(head)

    print("Duplicates Removed Output:")
    print_list(cleaned_head)