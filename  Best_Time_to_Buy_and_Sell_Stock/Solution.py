class Solution(object):



    prices =[5,1,2,9,3,12,1,5,100]

    def maxProfit(self, prices):
        reversed_prices = list(reversed(prices[:]))
        BuyPrice1 =  prices[0]
        SellPrice1=0
        BuyPrice2 =0
        earning = []

        """
        :type prices: List[int]
        :rtype: int     
        """
        for i,price in enumerate(prices[1:]):                       # todo: Optimize to O(n)
            BuyPrice1 = min(prices[0:i+1])
            SellPrice1 = max(prices[i:len(prices)])
            earning.append(SellPrice1 - BuyPrice1)

        if earning == [] or int(max(earning))<0:
            return 0
        else:
            return int(max(earning))

    print(maxProfit(None,prices))