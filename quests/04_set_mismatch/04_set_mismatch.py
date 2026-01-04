from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        seen = set()
        dup = 1

        for i in nums:
            if i in seen:
                dup = i
                continue
            else:
                seen.add(i)
        n = len(nums)
        missing = abs(n*(n+1)//2 - sum(seen))
        return [dup,missing]
            

if __name__ =="__main__":
    s = Solution()
    print(s.findErrorNums([1,2,2,4]))
    print(s.findErrorNums([1,1]))