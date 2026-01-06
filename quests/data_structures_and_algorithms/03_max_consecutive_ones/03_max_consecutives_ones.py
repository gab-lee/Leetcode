from typing import List

class Solution:
    def findZeroPosition(self,nums)-> List:
        zero_pos = []
        count = 0
        for i in nums:
            if i == 0:
                zero_pos += [count+2]
            count += 1 
        return zero_pos
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zero_pos=[1]+self.findZeroPosition(nums)+[len(nums)+2]
        consecutive_ones = []
        for i in range(len(zero_pos)-1):
            consecutive_ones += [zero_pos[i+1]-zero_pos[i]-1]
        return (max(consecutive_ones))
            
if __name__ == "__main__":
    s = Solution()
    
    print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))          
    print(s.findMaxConsecutiveOnes([1,0,1,1,0,1]))