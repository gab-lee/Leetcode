class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        best = 0
        for i,p in enumerate (prices):
            if p < low: 
                low = p
            else: 
                best = max(best, p-low) # update only if profit better than current best
        return best
            
if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4])) #5
    print(s.maxProfit([7,6,4,3,1])) #0
    print(s.maxProfit([7,3,5,1,6,4])) #5