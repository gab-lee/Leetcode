class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i]+1
                return digits
        return [1] + digits

if __name__ == "__main__":
    s = Solution()

    print(s.plusOne([1,2,3])) # [1,2,4]
    print(s.plusOne([1,2,9])) # [1,3,0]
    print(s.plusOne([1,9,9])) # [1,3,0]
    print(s.plusOne([9,9,9])) # [1,3,0]