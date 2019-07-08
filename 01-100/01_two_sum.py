# -*- coding: UTF-8 -*-

class Solution:
    # my ugly code
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in nums:
            i = nums.index(num)
            for n in nums[i:]:
                if num + n == target:
                    return[i, nums.index(n)]

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
    nums = [2, 7, 11, 15]
    target = 9

    result_list = Solution().twoSum(nums, target)
    print(result_list)

if __name__ == '__main__':
    main()

