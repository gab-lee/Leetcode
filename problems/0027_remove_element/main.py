class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in (range(len(nums) -1,-1,-1)):
            print(nums[i])
            if nums[i] != val:
                count +=1
                continue
            else:
                nums.pop(i)
        return count
if __name__ == "__main__":
    s = Solution()

    print(s.removeElement([3,2,2,3],3))
    print(s.removeElement([0,1,2,2,3,0,4,2],2))