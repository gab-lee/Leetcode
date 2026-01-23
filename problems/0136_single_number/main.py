class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Time: O(n) Space: O(1)
        #use XOR
        ans = 0
        for n in nums:
            ans ^= n
        return ans
        
if __name__ == "__main__":
    s = Solution()

    print(s.singleNumber([2,2,1])) #1
    print(s.singleNumber([4,1,2,1,2])) #4
    print(s.singleNumber([0,0,1])) #1