class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = [] 
        for num in range(left,right+1):
            ispass = False
            for digit in str(num):
                if int(digit)==1:
                    ispass = True
                elif int(digit) ==0:
                    ispass = False
                    break
                elif num % int(digit) ==0:
                    ispass = True
                else:
                    ispass = False
                    break
            if ispass:
                ans += [num]

        return ans
        
if __name__ == "__main__":
    s = Solution()

    print("Test case")
    print(s.selfDividingNumbers(1,2))
    print(s.selfDividingNumbers(47,85))