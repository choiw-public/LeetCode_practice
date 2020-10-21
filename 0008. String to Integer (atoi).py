class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # step0: discard beginning white spaces
        # step1: consider plus or minus sign followed by as many numerical digits as possible
        # step2: interpret them a s a numerical value

        # additional characters after integral number are ignored
        # if no sequence exists or the first sequence is not number, no conversion.

        # no conversion -> zero.
        s = s.strip()

        if not s:
            return 0

        sign = 1
        if '-' == s[0]:
            sign = - 1
            s = s[1::]
        elif '+' == s[0]:
            s = s[1::]

        # iterate until meet a character
        num = ""
        for letter in s:
            if letter.isnumeric():
                num += letter
            else:
                break
        if num:
            num = int(float(num)) * sign
            return min(max(-2 ** 31, num), 2 ** 31 - 1)
        else:
            return 0


s = Solution()
s.myAtoi("3.14159")
