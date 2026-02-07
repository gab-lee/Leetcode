from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_distance = 0
        end_point = len(nums)-1
        for i, n in enumerate(nums):
            max_distance = max(max_distance,i+n)
            if max_distance >= end_point:
                return True
            elif max_distance == i and n == 0:
                return False
        return False

if __name__ == "__main__":
    s= Solution()

    print(s.canJump([3,1,0,1])) #True
    print(s.canJump([2,3,1,1,4])) #True
    print(s.canJump([3,2,1,0,4])) #False
    print(s.canJump([3,0,8,2,0,0,1])) #True
            
            


            
