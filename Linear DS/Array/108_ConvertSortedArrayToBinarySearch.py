from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        def build_bst(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)
            return root
        return build_bst(0, len(nums) - 1)

def level_order_print(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Strip trailing None values for cleaner reading
    while result and result[-1] is None:
        result.pop()
    return result

if __name__ == "__main__":
    sol = Solution()
    
    t1 = [-10, -3, 0, 5, 9]
    tree1 = sol.sortedArrayToBST(t1)
    
    t2 = [1, 3]
    tree2 = sol.sortedArrayToBST(t2)
    
    print("-" * 50)
    print(f"Input: {t1} -> Level-Order: {level_order_print(tree1)}")
    print(f"Input: {t2}           -> Level-Order: {level_order_print(tree2)}")
    print("-" * 50)


















