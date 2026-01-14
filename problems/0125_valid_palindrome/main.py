class Solution:
    def format_string(self, s:str) -> str:
        #remove non-alphanumeric characters (including space)
        s = "".join(ch for ch in s if ch.isalnum())
        #convert to lowercase
        s = s.lower()
        
        return s

    def isPalindrome(self, s: str) -> bool:
        s = self.format_string(s)
        #print(f"formatted string: {s}")
        return s == s[::-1]

if __name__ == "__main__":
    s = Solution()

    print(s.isPalindrome(" ")) #expect True
    print(s.isPalindrome(" A ")) #expect True
    print(s.isPalindrome("A man, a plan, a canal: Panama")) #expect True
    print(s.isPalindrome("race a car")) #expect False
        