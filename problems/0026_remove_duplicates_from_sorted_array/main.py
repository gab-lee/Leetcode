class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        target = None

        for i in range(len(nums)-1,-1,-1): #go backwards in sorted list
            if target == None:
                target = nums[i]
                continue
            elif (target == nums[i]):
                nums.pop(i)
            else:
                target = nums[i]
                #print(f"target take new value{target},{nums[i]}")
        
        #print(nums)
        return len(nums)
        


if __name__ == "__main__":
    s = Solution()
    
    print(s.removeDuplicates([1,1,2]))
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(s.removeDuplicates([1]))
    print(s.removeDuplicates([1,1,1,1,1,1,1]))