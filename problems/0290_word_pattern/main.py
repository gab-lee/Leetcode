class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        d = {}
        seen = set()
        
        if len(s) > len(pattern) or len(s) < len(pattern):
            return False

        for key,target in zip(pattern,s):
            if key not in d:
                if target in seen:
                    return False #already matched with something 
                else:
                    d[key]=target #otherwise create pair 
                    seen.add(target)
            elif d[key]!=target:
                return False 
        return True

if __name__ == "__main__":
    s = Solution()

    print(s.wordPattern("abba","dog cat cat dog")) #True
    print(s.wordPattern("abba","dog cat cat fish")) #False
    print(s.wordPattern("aaaa","dog cat cat dog")) #False
    print(s.wordPattern("abba","dog dog dog dog")) #True