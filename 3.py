My code:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        sub_s = {}
        sub_s_ = []
        for i in s:
            while s[i] != s[i+1]:
                sub_s_.append(s[i])
                for i in sub_s_:
                    if s[i] = sub_s[i]:
                        return None
                    sub_s.append(sub_s_)
        best_sub = max(len(sub_s))
        length = len(best_sub)
                
        return best_sub, length


ANSWER:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last = {}        # 记录字符最近出现的下标: char -> index
        left = 0         # 当前窗口左边界
        best = 0         # 最长长度

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1      # 左边界跳过重复字符上次出现的位置

            last[ch] = right             # 更新 ch 的最新位置
            best = max(best, right - left + 1)

        return best
