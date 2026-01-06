class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        exp = arr[0]

        for i in arr:
            if i != exp:
                return False
            else: 
                exp += diff
        return True

if __name__ == "__main__":
    s = Solution()

    print(s.canMakeArithmeticProgression([3,5,1]))
    print(s.canMakeArithmeticProgression([1,2,4]))