class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        row 1 and row n will have the same number of characters 
        A Zig (down and diagonal up) is made up of n + n-2 characters 
        n sequence will look like
        ```
        0      6
        1    5 7 
        2  4   8 
        3      9
        
        next number is a triangle away 

        numsRow - row 
        ```
        """
        def nextCharacter(self,character_index,numRows):
            sequence = 2*numRows -2 
            pos = character_index % sequence
            if pos <= numRows -1:
                next_pos = character_index + 2*(numRows-1-pos)
            else:
                next_pos = character_index + 2*(sequence+1-pos)
            print(next_pos)
            return next_pos


        if len(s) <= 2: 
            return s

        conversion = ""
        
        row = 0
        for i in range (len(s)):
            if nextCharacter(self,i,numRows) < len(s):
                conversion += s[nextCharacter(self,i,numRows)]
            else:
                row +=1
                conversion += s[row]

        return conversion

if __name__ == "__main__":
    s = Solution()
    print(s.convert(s = "PAYPALISHIRING", numRows = 3))
    print(s.convert (s = "PAYPALISHIRING", numRows = 4))
    print(s.convert (s = "A", numRows = 1))