class Solution:
    def divide_by_div(self, n, div):
        while n % div == 0:
            n = n // div
        return n 
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n ==1:
            return True 
        else: 
            n=self.divide_by_div(n,2)
            print(n)
            n=self.divide_by_div(n,5)
            n=self.divide_by_div(n,7)
            if n == 1:
                return False
            else:
                return True 
        

if __name__ == "__main__":
    s = Solution()

    print(s.isUgly(8))
    print(s.isUgly(1))
    print(s.isUgly(14))