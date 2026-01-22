class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if n > h:
            return -1 

        for i in range(h):
            for j,ch in enumerate(needle):
                if (i+j >= h):
                    break
                elif ch != haystack[i+j]:
                    break
                elif j == n-1:
                    return i

        return -1

if __name__ == "__main__":
    s = Solution()

    print(s.strStr("sadbutsad","sad")) #0
    print(s.strStr("sabbutsasa","sad")) #0
    #print(s.strStr("leetcode","leeto")) #0