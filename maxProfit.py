class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cmb = prices[0]
        lucro_max = 0

        for preco in prices:
            if preco < cmb:
                cmb = preco
            elif (preco - cmb) > lucro_max:
                lucro_max = preco - cmb

        return lucro_max 

            

                

        