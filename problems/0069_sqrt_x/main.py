class Solution:
    def mySqrt(self, x: int) -> int:
        root = 0 
        while root <= x:
            square = root * root 
            if  square == x:
                return root
            elif square > x:
                return root - 1 
            else:
                root +=1 
        

if __name__ == "__main__":
    s = Solution()

    print(s.mySqrt(0)) #0
    print(s.mySqrt(1)) #1
    print(s.mySqrt(4)) #2
    print(s.mySqrt(3)) #2
    print(s.mySqrt(8)) #2
    