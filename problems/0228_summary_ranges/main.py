from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        #given nums is sorted, len(nums)>=0 
        ans = []
        temp = None

        #edge cases
        l = len(nums)
        if l == 0:
            return ans
        if l == 1:
            ans.append(str(nums[0]))
            return ans

        for i,n in enumerate(nums):

            if i +1 >= l: 
                break
            if n+1 != nums[i+1]: #standalone number
                if temp == None: 
                    ans.append(f"{n}")
                else:
                    ans.append(f"{temp}->{n}")
                    temp = None
            elif temp == None:
                temp = n
        
        if temp == None:
            ans.append(f"{n}")
            return ans
        else:
            ans.append(f"{temp}->{n}")
            return ans


if __name__ == "__main__":
    s = Solution()

print(s.summaryRanges([0,1,2,4,5,7])) #["0->2","4->5","7"]
print(s.summaryRanges([0,2,3,4,6,8,9])) #["0","2->4","6","8->9"]
print(s.summaryRanges([0])) #["0"]
print(s.summaryRanges([-1])) #["-1"]
print(s.summaryRanges([])) #[]