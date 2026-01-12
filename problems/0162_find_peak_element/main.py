class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # Remove edge cases
        if len(nums) == 1: # single element
            return 0
        elif nums[0] > nums[1]: #peak is at the start
            return 0
        elif nums[-1] > nums[-2]: #peak is at the end
            return len(nums)-1 
        
        # Peak is within the array
        n = len(nums) 
        low , high = 0, n -1
        while low <= high:
            #print(f"low: {low}, high: {high}")
            mid = (low+high)//2
            target = nums[mid]
            #print(f"mid: {mid}, target: {target}")
            #print(f"before: {target > nums[mid-1]}, after: {target > nums[mid+1]}")

            if target > nums[mid-1] and target > nums[mid+1]: # Peak is greater than number before and after it
                return mid 
            
            elif target < nums[mid+1]: # ascending 
                low = mid +1 # exclude mid 

            else:
                high = mid -1 # exclude mid 
        return -1

        
if __name__ == "__main__":
    s = Solution()

    #nums[i] != nums[i + 1] for all valid i. No consequitive repetitive number
    print(s.findPeakElement([1])) #Output: 0
    print(s.findPeakElement([7,2,3,1])) #Output: 0
    print(s.findPeakElement([1,2,3,7])) #Output: 3
    print(s.findPeakElement([1,2,3,1])) #Output: 2
    print(s.findPeakElement([1,2,1,3,5,6,4])) #Output: 5
    print(s.findPeakElement([1,2,1,3,4,5,6])) #Output: 1
    print(s.findPeakElement([1,2,1,3,2])) #Output: 1 or 3