class Solution {
    func canCompleteCircuit(_ gas: [Int], _ cost: [Int]) -> Int {
        //Given it is a circular route, compute gas debt
        var tank: Int = 0
        var currentTank: Int = 0
        var startPos: Int = 0
        for i in 0..<gas.count{
            let tripCost: Int = gas[i] - cost[i]
            tank += tripCost

            //Viability of start point        
            currentTank += tripCost
            if currentTank < 0 {
                startPos = i+1
                currentTank = 0
            }
            
        }
        return tank >= 0 ? startPos : -1
    }
}

let s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))