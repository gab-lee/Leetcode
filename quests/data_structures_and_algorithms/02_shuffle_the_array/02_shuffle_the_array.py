from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        sorted_nums=[]
        for i in range(n):
            sorted_nums += [nums[i],nums[i+n]]
        return sorted_nums

if __name__ == "__main__":
    s = Solution()

    print(s.shuffle([2,5,1,3,4,7],3)) 

        