# -*- coding: UTF-8 -*-

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: list
        :type nums2: list
        :rtype : float
        """
        # may be wrong
        new_nums = sorted(nums1 + nums2)
        new_nums_len = len(new_nums)
        if new_nums_len % 2 == 0:
            return (new_nums[new_nums_len//2-1] + new_nums[new_nums_len//2]) / 2
        else:
            return new_nums[(new_nums_len)//2]

def main():
    nums1 = [1, 3]
    nums2 = [2]
    result = Solution().findMedianSortedArrays(nums1, nums2)
    print(str("%.1f" % result))

if __name__ == '__main__':
    main()