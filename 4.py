My code:
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import numpy as np

        total_nums = np.array(nums1, nums2)
        total_nums.sort()

        if len(nums1) > 1000 and len(nums2) > 1000:
            return None

        value = total_nums % 2
        length = len(total_nums)
        half_length = length / 2
        if value !=0:
            # means it is odd
            index = half_length -1
            for index, x in enumerence(total_nums):
                median_index = total_number[index]
                median_value = total_number[x]
        else:
            # means it is even
            for i, x in enumerence(total_nums):
                median_1 = total_number[index]
                median_2 = total_number[index+1]
                median_value = (median_1 + median_2)/2
        
        return median_value



ANSWER:
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import numpy as np

        # 1) 合并成一个数组（你原来 np.array(nums1, nums2) 是错的）
        total_nums = np.array(nums1 + nums2, dtype=float)

        # 2) 排序
        total_nums.sort()

        # 3) 计算长度与中位数
        length = len(total_nums)
        half = length // 2

        if length % 2 == 1:
            # 奇数：中间那个
            median_value = float(total_nums[half])
        else:
            # 偶数：中间两个平均
            median_value = (total_nums[half - 1] + total_nums[half]) / 2.0

        return median_value
