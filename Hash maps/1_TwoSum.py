class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

if __name__ == "__main__":
    sol = Solution()
    
    t1_nums, t1_target = [2, 7, 11, 15], 9
    t2_nums, t2_target = [3, 2, 4], 6
    t3_nums, t3_target = [3, 3], 6
    
    print("-" * 45)
    print(f"Test 1: nums={t1_nums}, target={t1_target} -> {sol.twoSum(t1_nums, t1_target)}")
    print(f"Test 2: nums={t2_nums}, target={t2_target}     -> {sol.twoSum(t2_nums, t2_target)}")
    print(f"Test 3: nums={t3_nums}, target={t3_target}     -> {sol.twoSum(t3_nums, t3_target)}")
    print("-" * 45)