My code:
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        import numpy as np

        # 不能这样写，因为一次只能拿一个下标，我这样就一次拿了两个下标
        for i, j in height:
            # 不能这样，只能height[i], height[j]
            new_height = height[i,j]
            volumn = abs((j-i)*min((height[i], height[j])))
            max_sum = max(volumn)
        print(max_sum)

        return max_sum


ANSWER:
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_sum = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                volumn = (j - i) * min(height[i], height[j])
                max_sum = max(max_sum, volumn)

        return max_sum
