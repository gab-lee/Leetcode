class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dict = [Int:Int]()
        //Iterate through nums (time: O(n))
        for (index,num) in nums.enumerated() {
            //Determine the complimentary number based on target (target-n)
            let complimnetary = target - num
            //Check if complimnetary number is in dict
            if dict.keys.contains(complimnetary){
                //Return index if it is in
                let complimentary_index = dict[complimnetary]! //force unwrap if not it will return an optional
                return [complimentary_index,index]
            }
            //Add number and index into dict
            dict[num]=index
        }
        //No number set can be found, return -1 (Should not happen since QN states exactly 1 sol)
        return [-1]
    }
}

let s = Solution()
print(s.twoSum([2,7,11,15],9))
print("Solution: [0,1]")
print(s.twoSum([3,2,4],6))
print("Solution: [1,2]")
print(s.twoSum([3,3],6))
print("Solution: [0,1]")