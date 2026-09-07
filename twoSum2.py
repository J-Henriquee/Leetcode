class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}

        for i, n in enumerate(numbers):
            complement = target - n
            if complement in num_map:
                return [num_map[complement] + 1, i + 1]
            num_map[n] = i

        