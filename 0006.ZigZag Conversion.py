class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ""
        str_out = ""

        for i in range(numRows):
            j, idx = 1, 0
            str_out += s[i]
            if numRows - 1 and len(str_out) < len(s):
                idx = i + 2 * (numRows - 1) * j
                while idx < len(s) or (idx - i * 2) < len(s):
                    if 0 < i < numRows - 1:
                        str_out += s[idx - i * 2]
                    if idx < len(s):
                        str_out += s[idx]
                    j += 1
                    idx = i + 2 * (numRows - 1) * j
        return str_out


s = Solution()
print(s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
print(s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
print(s.convert("0", 1))
