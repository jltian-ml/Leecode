My code:
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        step = 0
        length = len(x)

        new_x = []
        for i, ch in enumerate(x):
            x[i] = len(x) - i
            new_x.append(x[ch])
        
        if x < 0:
            new_x = - abs(new_x)

        return new_x


ANSWER:
class Solution(object):
    def reverse(self, x):
        INT_MIN = -2**31
        INT_MAX =  2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0
        while x != 0:
            pop = x % 10
            x //= 10

            # 检查 rev*10 + pop 是否会超过 INT_MAX
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
                return 0

            rev = rev * 10 + pop

        rev *= sign
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev
