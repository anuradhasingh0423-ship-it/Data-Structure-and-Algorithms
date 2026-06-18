class NumArray:
    def __init__(self, nums: list[int]):
        # Create a prefix sum array with an extra 0 at the start
        self.prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]

    def sum_range(self, left: int, right: int) -> int:
        # Formula: Sum(L, R) = Prefix[R + 1] - Prefix[L]
        return self.prefix_sums[right + 1] - self.prefix_sums[left]

# Example usage:
obj = NumArray([1, 2, 3, 4, 5])
print(obj.sum_range(1, 3))  # returns 9 (2 + 3 + 4)