class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        # min: replace all occurrences of the first digit with 0
        min_num = int(s.replace(s[0], "0")) 

        # max: replace all occurrences of first non-9 digit with 9
        target = None
        for ch in s:
            if ch != "9":
                target = ch
                break

        # if all digits are 9, max is the number itself
        max_num = num if target is None else int(s.replace(target, "9"))
    
        return max_num-min_num
        
if __name__ == "__main__":
    s = Solution()

print(s.minMaxDifference(11891)) #Expect 99009