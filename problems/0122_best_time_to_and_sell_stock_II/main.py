from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))#7
    print(s.maxProfit([1,2,3,4,5]))#4
    print(s.maxProfit([7,6,4,3,1]))#0
    print(s.maxProfit([7]))#0
    print(s.maxProfit([2,6,8,7,8,7,9,4,1,2,4,5,8]))#0