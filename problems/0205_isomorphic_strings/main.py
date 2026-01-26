class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
    #Given: t.length == s.length
    #Given: s.length >= 1
        d = {}
        used = set()

        for a,b in zip(s,t):
            if a not in d:
                if b in used:
                    return False 
                else:
                    d[a] = b
                    used.add(b)
            elif d[a] != b:
                return False
            
        return True

if __name__ == "__main__":
    s = Solution()

    print(s.isIsomorphic("egg","add")) #True
    print(s.isIsomorphic("foo","bar")) #False
    print(s.isIsomorphic("paper","title")) #True
    print(s.isIsomorphic("bbbaaaba","aaabbbba")) #False