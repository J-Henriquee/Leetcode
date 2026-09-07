class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_map = {}
        for n in nums:
            if n not in nums_map:
                nums_map[n] = 1
            else:
                nums_map[n] += 1
        for n in nums:
            if nums_map[n] == 1 and (n % 2) == 0:
                return n
        return -1
