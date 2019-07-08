# -*- coding: UTF-8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype : int
        """
        s_list = list(s)
        d = {}
        last_sub_str_len = 0
        cur_sub_str_len = 0
        max_sub_str_len = 0
        for i, letter in enumerate(s_list):
            if letter in d:
                cur_sub_str_len = i - d[letter]
            # Every time the value of dict same key will be changed.
            d[letter] = i
            max_sub_str_len = max(cur_sub_str_len, last_sub_str_len, max_sub_str_len)
            last_sub_str_len = cur_sub_str_len
        return max_sub_str_len

def main():
    s = "abcabcbb"
    result = Solution().lengthOfLongestSubstring(s)
    print(result)

if __name__ == '__main__':
    main()