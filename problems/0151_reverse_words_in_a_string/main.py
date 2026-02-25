class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = words[::-1]
        words = " ".join(words)
        return words

if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("the sky is blue"))
    print(s.reverseWords("  hello world  "))
    print(s.reverseWords("  hello 2  "))