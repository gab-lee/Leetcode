from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        product at Index = Left[Index] x Right[Index]
        """
        answer = [1] * len(nums)

        left = 1
        for i in range (len(nums)):
            answer[i] = left
            left *= nums[i]
        
        right = 1
        for j in range (len(nums)-1,-1,-1):
            answer[j] *= right
            right *= nums[j]
        
        return answer

if __name__ == "__main__":
    s = Solution()

    print(s.productExceptSelf([1,2,3,4]))
    print(s.productExceptSelf([-1,1,0,-3,3]))