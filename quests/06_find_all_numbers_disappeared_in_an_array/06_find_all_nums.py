from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        expected_nums = {i:0 for i in range(1,len(nums)+1)}
        for i in nums:
            expected_nums[i]=1

        return [k for k, v in expected_nums.items() if v==0]

        
if __name__ == "__main__":
    s = Solution()

    print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    print(s.findDisappearedNumbers([1,1]))
    print(s.findDisappearedNumbers([1,2]))