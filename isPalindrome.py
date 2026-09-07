class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        s = str(x)
        esq = 0
        dir = len(s) - 1

        while dir > esq:
            if s[esq] != s[dir]:
                return False
            else:
                esq += 1
                dir -= 1
        return True

            
        
        containsDuplicate
        