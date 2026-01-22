class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        exception={'I':['V','X'],'X':['L','C'],'C':['D','M']}
        sum = 0
        for i,r in enumerate(s):
            if (r == 'I' or r == 'X' or r == 'C') and i != len(s)-1:
                if s[i+1] in exception[r]:
                    sum -= d[r]
                    #print("exception")
                    #print(sum, r, s[i+1])
                else:
                    #print(f"Should be normal {r}")
                    sum += d[r]    
            else:    
                #print(f"normal {r}")
                sum += d[r]
        return sum

if __name__ == "__main__":
    s = Solution()

    print(s.romanToInt("III")) #3
    print(s.romanToInt("LVIII")) #58
    print(s.romanToInt("MCMXCIV")) #1994
