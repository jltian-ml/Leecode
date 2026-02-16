My code:
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        direct = {}
        # the number of each whole set
        num = 2 * numRows - 2 
        for i, x in enumerate(s):
            while s[x] not in direct:
                direct = s[x]
                i += num

            if s[x] is in diect:
                s[x] = i + 1
                while s[x] not in direct:
                direct = s[x]
                i += num

        return direct


ANSWER:
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        row = 0
        step = 1  # 1 表示向下，-1 表示向上

        for ch in s:
            rows[row] += ch

            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1

            row += step

        return "".join(rows)
