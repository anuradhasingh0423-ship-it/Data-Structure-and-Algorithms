# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
            
        slow = head
        fast = head
        has_cycle = False
        
        # Step 1: Cycle I Detection
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
                
        # If no cycle was found, there's no entry point to look for
        if not has_cycle:
            return None
            
        # Step 2: Reset one pointer to the head
        fast = head
        
        # Step 3: Walk both at equal speed (1 step) until they meet
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        # Return either pointer, as both are now sitting on the loop entry node
        return slow