# Given the root of a binary search tree,
# and an integer k, return the kth smallest 
# value (1-indexed) of all the values of
# the nodes in the tree.


class Solution(object):
    def kthSmallest(self, root, k):

        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val

            curr = curr.right

if __name__ == "__main__":
    # Example usage:
    # Constructing a simple BST for demonstration
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # Creating a BST: 
    #       3
    #      / \
    #     1   4
    #      \
    #       2
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)

    sol = Solution()
    
    k = 1
    print(f"The {k}th smallest element is: {sol.kthSmallest(root, k)}")  # Output: 1

    k = 2
    print(f"The {k}th smallest element is: {sol.kthSmallest(root, k)}")  # Output: 2

    k = 3
    print(f"The {k}th smallest element is: {sol.kthSmallest(root, k)}")  # Output: 3

    k = 4
    print(f"The {k}th smallest element is: {sol.kthSmallest(root, k)}")  # Output: 4