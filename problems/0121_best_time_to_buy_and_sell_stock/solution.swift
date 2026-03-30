class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        //Skip impossible case
        if prices.count == 1 {
            return 0
        }
        //initialilse left and right pointers
        var left: Int = 0
        var right: Int = 1
        var max_profit: Int = 0
        //iterate n-1 times, so right pointer doesn't go out of frame
        for _ in 0..<prices.count - 1 {
            //determine profit 
            max_profit = max(max_profit, prices[right]-prices[left])
            //shift L pointer if currently buying high selling low
            if prices[left] >= prices[right]{
                left = right
                right += 1
            }
            //default, right pointer moves 1 to the right
            else{
                right += 1
            }
        }
        return max_profit
    }
}

let s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print("Solution: 5")
print(s.maxProfit([7,6,4,3,1]))
print("Solution: 0")