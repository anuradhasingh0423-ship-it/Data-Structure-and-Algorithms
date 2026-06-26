class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head
        
        # Loop runs as long as fast hasn't reached the end (None) 
        # AND fast hasn't landed on the very last node (fast.next is None)
        while fast is not None and fast.next is not None:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps (twice as fast)
            
        # When the loop stops, 'slow' is pointing directly at the middle node
        return slow