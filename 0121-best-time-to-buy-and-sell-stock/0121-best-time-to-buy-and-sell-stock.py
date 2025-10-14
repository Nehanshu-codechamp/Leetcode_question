class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Max_profit =0
        # n = len(prices)
        # for i in range (0,n):
        #     for j in range(i+1,n):
        #         if prices[j]>prices[i]:
        #            Max_profit = max(prices[j] -  prices[i], Max_profit)

        # return Max_profit           

        # optimal solution using one loop
        max_profit =0
        min_price = float("inf")
        n= len(prices)
        for i in range (0,n):
            min_price =min(min_price,prices[i])
            max_profit = max(max_profit , prices[i]-min_price)

        return max_profit    