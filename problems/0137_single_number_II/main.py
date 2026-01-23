class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Time: O(n) Space: O(1) -> no sets
        #XOR uses bit (Log 2) 
        #create a XOR using log 3 0,1,2
        
        store = 0 
        for n in nums:
            while n > 0:
                store += n%3
                n = n // 3
            print(store)
        return store


if __name__ == "__main__":
    s = Solution()

    print(s.singleNumber([2,2,3,2])) #3