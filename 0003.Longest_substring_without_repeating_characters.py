class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                # check length from start of string to index
                res = max(res, i - start)
                # update start of string index to the next index
                start = max(start, dic[ch] + 1)
            # add/update char to/of dictionary
            dic[ch] = i
        # answer is either in the begining/middle OR some mid to the end of string
        return max(res, len(s) - start)

    def practice(self, s):
        h_table, start, max_l = {}, 0, 0

        for i, letter in enumerate(s):
            if letter in h_table:
                max_l = max(max_l, i - start)
                start = max(start, h_table[letter] + 1)
            h_table[letter] = i
        return max(max_l, len(s) - start)

    def practice2(self, s):
        """
        :type s: str
        :rtype: int
        """
        h_table = {}
        longest_str = ""
        start_idx = 0
        for i, letter in enumerate(s):
            if letter in h_table:
                # this is important
                start_idx = max(start_idx, h_table[letter] + 1)
            h_table[letter] = i
            current_str = s[start_idx:i + 1]
            if len(longest_str) < len(current_str):
                longest_str = current_str


s = Solution()
print(s.lengthOfLongestSubstring("abcbad"))
print(s.practice("abcbefaaa"))
print(s.practice2("abcbefaaa"))
