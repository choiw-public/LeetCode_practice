'''
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = '-' + str(abs(x))[::-1]
        else:
            x = str(abs(x))[::-1]
        x = int(x)

        if not -2 ** 31 <= x <= 2 ** 31 - 1:
            return 0
        return x
