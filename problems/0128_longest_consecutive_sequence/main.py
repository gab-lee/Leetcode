from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Approach O(n) time
        
        """
        max = 0
        s = set(nums)
        l = len(s)
        #edge cases
        if l == 0 or l == 1:
            return l
        #main approach
        for n in s:
            if n -1 not in s: #begining 
                current = n
                length = 1
                while current+1 in s:
                    length += 1 
                    current += 1 
                if length > max:
                    max = length
                if max > l//2:
                    return max
                
            else:
                continue
        return max

if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([100,4,200,1,3,2])) #4
    print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) #9
    print(s.longestConsecutive([1,0,1,2])) #3
    print(s.longestConsecutive([2])) #1
    print(s.longestConsecutive([2,2,2,2,2])) #1
    print(s.longestConsecutive([1,2])) #2
    print(s.longestConsecutive([6,7,8])) #3
    print(s.longestConsecutive([1,2,6,7,8])) #3
    print(s.longestConsecutive([1,100])) #1