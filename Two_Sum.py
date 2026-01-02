from typing import List

class Solution:
    def num_too_big(self,num,target):
        if num > target:
            return True
        else:
            return False
    def twoSum(self, nums: List[int], target: int) -> list[int]:
        list_len = len(nums)
        for i in range(list_len):
            a = nums[i]
            if self.num_too_big(a,target):
                continue
            for j in range(list_len-i-1):
                b=nums[j+i+1]
                if self.num_too_big(b,target):
                    continue
                if (a+b == target):
                    return [i,i+j+1]
                else:
                    continue


if __name__ == "__main__":
    s = Solution()

    print(s.twoSum([2, 7, 11, 15], 9))   # expected [0, 1]
    print(s.twoSum([3, 2, 4], 6))        # expected [1, 2]
    print(s.twoSum([3, 3], 6))           # expected [0, 1]
    print(s.twoSum([-3,4,3,90], 0))           # expected [0, 1]