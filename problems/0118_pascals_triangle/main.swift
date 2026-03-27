class Solution {
    func generate(_ numRows: Int) -> [[Int]] {
        var result = [[Int]]()
        for row in 1...numRows{
            var rowArray = [Int]()
            for pos in 1...row{
                if pos == 1 || pos == row{
                    rowArray.append(1)
                }
                else{
                    let num = result[row-2][pos-2] +
                                result[row-2][pos-1]
                    rowArray.append(num)
                }
            }
            result.append(rowArray)
        }
        
        return result
    }
}

let s = Solution()
print(s.generate(7))