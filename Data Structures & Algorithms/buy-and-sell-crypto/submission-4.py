class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy, pMax = prices[0], 0

        for price in prices:
            pMax = max(pMax, price - minBuy)
            minBuy = min(minBuy, price)

        return pMax