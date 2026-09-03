class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_map = {}
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums_map:
              return [nums_map[complement], i]

            nums_map[n] = i