import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s =  re.sub(r'[^\w]', '', s).lower()
        p1 = 0
        p2 = len(s) - 1


        

        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            else:
                p1 += 1
                p2 -= 1
        return True

