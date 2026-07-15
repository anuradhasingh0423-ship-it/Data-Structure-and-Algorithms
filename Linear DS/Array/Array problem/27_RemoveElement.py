class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    target_val = 2
    
    print("-" * 40)
    print(f"Original Array: {nums}")
    print(f"Value to remove: {target_val}")
    
    solution = Solution()
    k = solution.removeElement(nums, target_val)
    
    print("-" * 40)
    print(f"Returned length (k): {k}")
    print(f"Modified array space (first k elements): {nums[:k]}")
    print(f"Full array state in memory: {nums}")
    print("-" * 40)