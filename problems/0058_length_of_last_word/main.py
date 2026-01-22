class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        clean = s.split()
        return len(clean[-1])

if __name__ == "__main__":
    s = Solution()

    print(s.lengthOfLastWord("Hello World")) #5
    print(s.lengthOfLastWord("   fly me   to   the moon  ")) #4
    print(s.lengthOfLastWord("luffy is still joyboy")) #6