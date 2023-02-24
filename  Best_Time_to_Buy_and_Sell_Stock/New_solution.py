class Solution:
    prices = [7,6,4,3,15]
    def maxProfit(self,prices): # The biggest difference of elements in list n, n[l] - n[r], where l>r.
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
