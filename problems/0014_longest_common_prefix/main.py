class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        key = strs[0]
        strs.pop(0)

        for i,ch in enumerate(key):
            p = ch
            for j in strs:
                if i > len(j) -1:
                    return "".join(prefix)
                elif j[i] != p:
                    return "".join(prefix)
            prefix.append(ch)
        return "".join(prefix)
        
        
if __name__ == "__main__":
    s = Solution()

    print(s.longestCommonPrefix(["flower","flow","flight"])) #"fl"
    print(s.longestCommonPrefix(["dog","racecar","car"])) #""
    print(s.longestCommonPrefix(["flower","flowe","fl"])) #"fl"
