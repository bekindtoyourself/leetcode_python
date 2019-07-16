# -*- coding: UTF-8 -*-

class Solution:
    # other guy wonderful code
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return[d[target-num], i]
            d[num] = i

def main():
    nums = [3,3]
    target = 6

    result_list = Solution().twoSum(nums, target)
    print(result_list)

if __name__ == '__main__':
    main()

