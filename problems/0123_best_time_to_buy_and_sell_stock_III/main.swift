class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        //skip impossible case
        if prices.count == 1 {
            return 0 
        }
    }
}


//Test cases
let s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))
print("Solution: 6")
print(s.maxProfit([1,2,3,4,5]))
print("Solution: 4")
print(s.maxProfit([7,6,4,3,1]))
print("Solution: 0")