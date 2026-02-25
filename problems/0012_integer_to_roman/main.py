class Solution:
    def intToRoman(self, num: int) -> str:
        d ={1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M"
            }
        
        roman = ""
        log = 0

        while num:
            #iterate through the digits starting from the back 
            digit = num % 10
            num = num //10
            if digit == 0:
                pass
            elif digit % 5 == 0:
                #direct search from dictionary 
                roman = d[digit * 10 ** log] + roman 
            elif digit == 4 or digit == 9:
                roman = d[(digit+1) * 10 ** log] + roman 
                roman = d[1 * 10 ** log] + roman 
            else: #1-3
                for i in range (digit % 5): 
                    roman = d[1 * 10 ** log] + roman 
                if digit > 5:
                    #add the 5 character
                    roman = d[5 * 10 ** log] + roman 
            log += 1 
        return roman 

if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3749))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))