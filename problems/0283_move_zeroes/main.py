from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        alias = nums 
        write_index = 0
        l = len(nums)

        #move non-zero in front and remove all zeroes
        for i in range(l):
            if nums[i] != 0:
                nums[write_index] = nums[i]
                write_index +=1   

        for i in range (write_index,l):
            nums[i] = 0 

        print(alias is nums)
        print(nums)
        
if __name__ == "__main__":
    s = Solution()
    s.moveZeroes([0,1,0,3,12])
