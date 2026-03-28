class Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {
        //Store solutions in res
        var res = [[Int]]()
        //sort list in preparation of 2 pointer Time: O(n)
        let sorted = nums.sorted()

        //Fix 1 number, thereby converting problem to 2Sum 
        for i in 0..<sorted.count {
            //Skip duplicates, question is only interested in unique solutions
            if i > 0 && sorted[i] == sorted[i-1] {
                continue
            }
            //skip impossible cases
            if sorted[i] > 0 {
                break
            }
            //two pointers
            var left = i + 1
            var right = sorted.count - 1
            while left < right {
                let sum = sorted[i] + sorted[left] + sorted[right]
                if sum == 0{
                    res.append([sorted[i],sorted[left],sorted[right]])
                    //skip duplicates for left and right pointers
                    left += 1
                    right -= 1 
                    while left < right && sorted[left] == sorted[left-1]{
                            left += 1
                    }
                    while left < right && sorted[right] == sorted[right+1]{
                            right -= 1
                    }
                } else if sum < 0 {
                    //increase sum by moving left pointer 
                    left += 1
                } else {
                    //increase sum by moving right pointer 
                    right -= 1
                }
            }
            
        }
        return res
    }
}

let s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print("Solution: [[-1,-1,2],[-1,0,1]]")
print(s.threeSum([0,1,1]))
print("Solution: []")
print(s.threeSum([0,0,0]))
print("Solution: [[0,0,0]]")
print(s.threeSum([0,0,0,0]))
print("Solution: [[0,0,0]]")