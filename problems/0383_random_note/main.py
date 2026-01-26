class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}

        if len(ransomNote)> len(magazine):
            return False

        for ch in magazine:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] +=1 

        for ch in ransomNote:
            if ch not in d:
                return False
            elif d[ch] == 0:
                return False 
            else:
                d[ch] -=1

        return True


if __name__ == "__main__":
    s = Solution()

    print(s.canConstruct("a","b"))
    print(s.canConstruct("aa","ab"))
    print(s.canConstruct("aa","aab"))