class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0 #index value of num
        high = len(nums) 

        while low < high: #binary search O(log(n)) time
            mid = (low+high)//2 # become mid of low and high 
            print (f"high: {high} low: {low} mid: {mid} target: {target}")
            if nums[mid] < target:
                low = mid +1 #exclude mid with +1
            else: #nums[mid] >= target
                high = mid 
        
        return low

if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1,3,5,6],5))
    print(s.searchInsert([1,3,5,6],2))
    print(s.searchInsert([1,3,5,6],7))
    print(s.searchInsert([1,3,5,6],-1))