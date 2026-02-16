My code:
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        string = {}
        # index number
        left = 0

        for i, x in enumerate(s):
            if x is not in string and len(x) >= 2:
                s[i] = left
                sub_string = s[left]
                string.append(sub_string)

        return string


ANSWER:
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        start = 0
        end = 0  # 最长回文的左右边界（包含）

        def expand(l, r):
            # 从中心 (l,r) 往两边扩，直到不是回文
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # 退出时 l,r 已经越过了回文边界，所以回文是 (l+1 .. r-1)
            return l + 1, r - 1

        for i in range(len(s)):
            l1, r1 = expand(i, i)       # 奇数
            l2, r2 = expand(i, i + 1)   # 偶数

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
