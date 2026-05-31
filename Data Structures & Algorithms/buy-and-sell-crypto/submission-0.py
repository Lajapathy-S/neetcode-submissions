class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res =[]
        # if prices = sorted(prices):
        #     return 0
        # else:
        for i in range (len(prices)):
            maxi = 0
            for j in range(i+1,len(prices)):
                temp = prices[j] - prices[i]
                maxi = max(maxi,temp)
            res.append(maxi)
        return max(res)
        