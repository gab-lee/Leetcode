from typing import List
class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Using a set iterate through nums to keep a list of seen elements
        return true if current element is in seen
        """
        seen = set()
        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                return True
        return False
    
if __name__ == "__main__":
    s= Solution()
    print(s.containsDuplicate([1,2,3,1])) #True
    print(s.containsDuplicate([1,2,3,4])) #False
    print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) #True
    print(s.containsDuplicate([1])) #False

