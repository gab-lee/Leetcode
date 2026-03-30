class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        //ignore impossible case
        if prices.count == 1 {
            return 0
        }
        //inialise left, right pointer
        var left: Int = 0
        var right: Int = 1
        //total profit will store total sum of profits
        var total_profits: Int = 0
        //iterate through prices.count
        while right < prices.count {
            //calculate profit 
            let cur_profit: Int = prices[right] - prices[left]
            //if cur trade is profitable add it to total profits
            if cur_profit > 0 {
                total_profits += cur_profit
                //debuggin
                //print("buy at \(prices[left]) sell at \(prices[right])")
                //move L,R pointer to after trade point (you can sell, then buy)
                left = right 
                right = left + 1
            }
            //trade is not profitable 
            //if Buying high and selling low, move left pointer to right pointer
            else if prices[left] >= prices[right]{
                left = right 
                right += 1
            }
        }
        return total_profits
    }
}

let s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print("Solution: 7")
print(s.maxProfit([1,2,3,4,5]))
print("Solution: 4")
print(s.maxProfit([7,6,4,3,1]))
print("Solution: 0")