class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            print(i)
            target = nums[-1]
            nums.pop(-1)
            nums.insert(0,target)
        print(nums)

if __name__ == "__main__":
    s = Solution()

    print(s.rotate([1,2,3,4,5,6,7],3))
    print(s.rotate([-1,-100,3,99],2))