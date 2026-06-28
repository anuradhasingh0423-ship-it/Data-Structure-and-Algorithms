# Given head, the head of a linked list, determine if the linked list has a cycle in it.


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next          
            fast = fast.next.next     
            
            if slow == fast:
                return True
        return False