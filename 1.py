my code:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        import numpy as np

        def data_validation(nums, target):
            if nums < 2 and nums > 10**4:
                return None
            if target <-10**9 and target > 10**9:
                return None
            else:
                reuturn nums, target

        self.nums = np.int(self.nums)
        self.target = np.int(self.target)

        nums, target = data_validation(self.nums, self.target)


        new_array = []
        for i, j in nums:
            value = target - nums[i]
            if value == nums[j]:
                return num[i], num[j]
            else:
                return None
            ner_array.append(num[i], num[j])
        
        return new_array

output = twoSum(self, nums, target)

print(output)


Answer:
class Solution(object):
    def twoSum(self, nums, target):
        # 可选：基本校验（不写也能过 LeetCode）
        # 如果超过这个数据范围的话就返回None
        if len(nums) < 2 or len(nums) > 10**4:
            return None
        if target < -10**9 or target > 10**9:
            return None

        # 建立空的字典
        seen = {}  # value -> index
        # 使用枚举，经历一遍nums里的所有值，enumerate(nums) 返回的每一项本来就是一个二元组 (index, value)，顺序固定
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i

        return None  # 理论上不会到这里（题目保证有解）


# 测试
s = Solution()
print(s.twoSum([2,7,11,15], 9))   # [0, 1]
print(s.twoSum([3,2,4], 6))       # [1, 2]
print(s.twoSum([3,3], 6))         # [0, 1]
