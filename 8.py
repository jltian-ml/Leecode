My code:
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        for i, x in enumerate(s):
            if s[x] == " ":
                return None
            elif s[x] != "-" or "+":
                return None
            elif s[x] == 0 and s[x-1] != int:
                return None
            elif s[0] != int:
                return 0
            else:
                return s[x]


ANSWER:
class Solution(object):
    def myAtoi(self, s):
        INT_MIN = -2**31
        INT_MAX =  2**31 - 1

        i = 0
        n = len(s)

        # 1) 跳过前导空格
        while i < n and s[i] == ' ':
            i += 1

        # 如果全是空格或空字符串
        if i == n:
            return 0

        # 2) 处理符号
        sign = 1
        if s[i] == '-' or s[i] == '+':
            if s[i] == '-':
                sign = -1
            i += 1

        # 3) 读取数字（遇到非数字就停）
        num = 0
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            # 4) 溢出检查（在乘10加digit之前判断）
            if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num
