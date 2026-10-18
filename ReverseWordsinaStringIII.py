class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        r, l = 0, 0
        reve = ""

        while r < len(s):

            if s[r] != " ":
                r += 1
            else:
                reve += s[l:r+1][::-1]
                r += 1
                l = r
        reve += " "
        reve += s[l:r+2][::-1]

        return reve[1:]
