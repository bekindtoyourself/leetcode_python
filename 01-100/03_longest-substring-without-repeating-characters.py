# -*- coding: UTF-8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype : int
        """
        d = {}
        max_sub_str_len = 0
        start = 0
        for i, letter in enumerate(s):
            if letter in d:
                start = max(start, d[letter] + 1)
            d[letter] = i
            max_sub_str_len = max(max_sub_str_len, i - start + 1)
        return max_sub_str_len

def main():
    # s = "asfbac"
    s = "abba"
    result = Solution().lengthOfLongestSubstring(s)
    print(result)

if __name__ == '__main__':
    main()