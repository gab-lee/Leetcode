class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pattern = 2*numRows-2
        if len(s) <= 2: 
            return s
        

if __name__ == "__main__":
    s = Solution()
    print(s.convert(s = "PAYPALISHIRING", numRows = 3))
    print(s.convert (s = "PAYPALISHIRING", numRows = 4))
    print(s.convert (s = "A", numRows = 1))