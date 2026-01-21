class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        target = None #to replace with a dict
        d = {}
        for i in range (len(nums)-1,-1,-1): #iterate backwards 
            if nums[i] not in d: 
                d[nums[i]] = 1
            elif d[nums[i]] == 2:
                nums.pop(i)
            else:
                d[nums[i]] += 1
        #print(nums)

        return len(nums) #remaining elements should be in first k index

if __name__ == "__main__":
    s = Solution()

    print(s.removeDuplicates([1,1,1,2,2,3])) #Return 5, [1,1,2,2,3,_]
    print(s.removeDuplicates([0,0,1,1,1,1,2,3,3])) #Rerturn 7, [0,0,1,1,2,3,3,_,_]