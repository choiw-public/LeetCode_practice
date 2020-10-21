"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        def helper(l, r):
            """
            Be careful. "s[l] == s[r]" should not be the beginning of the while statement below.
            """
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            return s[l + 1:r]

        res = ""
        for i in range(len(s)):
            test = helper(i, i)
            if len(test) > len(res): res = test
            test = helper(i, i + 1)
            if len(test) > len(res): res = test
        return res

    def practice(self, s):
        out_string = ""

        def spread(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            tmp = spread(i, i + 1)
            if len(tmp) > len(out_string):
                out_string = tmp
            tmp = spread(i, i)
            if len(tmp) > len(out_string):
                out_string = tmp
        return out_string

    def brute_force(self, s):
        # find all possible substrings
        # brute force solution
        if not s:
            return ""
        for window_length in range(len(s) + 1, 0, -1):
            for start_index in range(0, len(s) - window_length + 1):
                sub = s[start_index:start_index + window_length]
                if sub == sub[::-1]:
                    return sub

    def practice2(self, s):
        substrings = ""

        def spread(left, right):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            tmp = spread(i, i + 1)
            if len(tmp) > len(substrings):
                substrings = tmp
            tmp = spread(i, i)
            if len(tmp) > len(substrings):
                substrings = tmp
        return substrings


s = Solution()
best_anser = s.longestPalindrome("babad")
brute_force_solution_ans = s.brute_force("babad")
ans2 = s.practice2("a")
