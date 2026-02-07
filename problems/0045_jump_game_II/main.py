from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        maxDistance = 0
        current_end = 0
        for i in range(len(nums)-1):
            maxDistance = max(maxDistance,i+nums[i])
            if i == current_end:
                current_end = maxDistance
                jumps +=1
        return jumps

if __name__ == "__main__":
    s = Solution()
    print(s.jump([0])) #0
    print(s.jump([2,3,1,1,4])) #2
    print(s.jump([2,3,0,1,4])) #2
    print(s.jump([8,3,0,1,4])) #1
    print(s.jump([1,5,1,0,1])) #2
    print(s.jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3])) #2