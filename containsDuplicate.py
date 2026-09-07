class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        duplicate_map = set()
        for n in nums:
            if n in duplicate_map:
                return True
            duplicate_map.add(n)  
    
        return False