class Solution:
    def myPow(self, x: float, n: int) -> float:
        #edge case where result == x
        if x == 0 or x == 1:
            return x
        if n == 0:
            return 1
            
        #if n is negative convert x to fraction 
        if n < 0:
            x = 1/x
            n = abs(n)

        def helper(n,x):
            if n == 1:
                return x
            elif n % 2 == 0:
                temp = helper(n//2,x)
                return temp * temp
            else: 
                temp = helper((n-1)//2,x)
                return temp * temp * x

        return helper(n,x)

if __name__ == "__main__":
    s = Solution()

    print(s.myPow(2.00000,10)) #1024.00000
    print(s.myPow(2.10000,3)) #9.26100
    print(s.myPow(2.00000,-2)) #0.25000 
    print(s.myPow(2.00000,-1)) #0.5
    print(s.myPow(0.00000,-1)) #0
    print(s.myPow(5.00000,0)) #1
    print(s.myPow(0.00001,2147483647)) #0
    print(s.myPow(100,2147483647)) #