# 1. Define the Node structure LeetCode uses under the hood
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        pointerA = headA
        pointerB = headB

        while pointerA != pointerB:
            pointerA = headB if pointerA is None else pointerA.next
            pointerB = headA if pointerB is None else pointerB.next

        return pointerA


if __name__ == "__main__":
    # Let's recreate Example 1:
    # List A: 4 -> 1 -> [8 -> 4 -> 5]
    # List B: 5 -> 6 -> 1 -> [8 -> 4 -> 5]
    
    # Step A: Create the SHARED intersecting part first
    intersect_part = ListNode(8)
    intersect_part.next = ListNode(4)
    intersect_part.next.next = ListNode(5)

    # Step B: Create the unique front part of List A and link it to the shared part
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = intersect_part  # Linking to the shared '8' node

    # Step C: Create the unique front part of List B and link it to the shared part
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = intersect_part  # Linking to the exact same '8' node

    # Step D: Run the solution
    sol = Solution()
    intersection_node = sol.getIntersectionNode(headA, headB)

    # Step E: Verify and print output
    print("-" * 40)
    if intersection_node:
        print(f"✅ Success! Intersected at node with value: '{intersection_node.val}'")
        print(f"Memory Address of intersection: {hex(id(intersection_node))}")
    else:
        print("❌ No intersection found.")
    print("-" * 40)