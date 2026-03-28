class Solution {
    func twoSum(_ numbers: [Int], _ target: Int) -> [Int] {
        //solve using two pointers
        var left = 0
        var right = numbers.count - 1 
        
        while left < right {
            //calc sum of two numbers
            let sum = numbers[left] + numbers[right]
            //determine which pointer to move
            if sum == target{
                return [left+1,right+1] //index +1
            } else if sum < target{
                //increase sum by moving left pointer
                left += 1
            } else {
                //reduce sum by moving right pointer
                right -= 1
            }

        }
        return []
    }
}
let s = Solution()

print(s.twoSum([2,7,11,15],9))
print("Solution: [1,2]")
print(s.twoSum([2,3,4],6))
print("Solution: [1,3]")
print(s.twoSum([-1,0],-1))
print("Solution: [1,2]")
print(s.twoSum([12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997],542))
print("Solution: [1,2]")
