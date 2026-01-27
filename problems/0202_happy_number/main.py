class Solution:
    def isHappy(self, n: int) -> bool:
    #given n > 0
        seen = set()

        while n:
            sum = 0 
            n = str(n)
            for i in n:
                sum += int(i) ** 2
            
            if sum == 1:
                return True
            elif sum in seen:
                return False
            
            n = sum
            seen.add(n)
    
    
if __name__ == "__main__":
    s = Solution()
    #test cases
    print(s.isHappy(19)) # True
    print(s.isHappy(2)) # False