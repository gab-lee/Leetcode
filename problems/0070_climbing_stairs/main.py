class Solution:
    def climbStairs(self, n: int) -> int:
        #Bottom up Dynamic programming 
        
        one, two = 1,1
        
        for i in range (n-1): 
        #fibonaci series 
          temp = one
          one = one + two 
          two = temp
        
        return one
        
if __name__ == "__main__":
    s = Solution()

    print(s.climbStairs(1)) #2
    print(s.climbStairs(2)) #2
    print(s.climbStairs(3)) #3
    print(s.climbStairs(4)) #22,112,211,1111,121 #5