class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #edge cases
        if len(s) > len(t) or len(t) > len(s):
            return False
        
        #main 
        sdict ={}
        tdict ={}

        def addToDict(ch,dict):
            if ch not in dict:
                dict[ch]=1
            else:
                dict[ch]+=1
         
        for a,b in zip(s,t):
            addToDict(a,sdict)
            addToDict(b,tdict)
        
        for k,v in sdict.items():
            if k not in tdict or tdict[k]!=v:
                return False
        
        return True


if __name__ == "__main__":
    s = Solution()

    print(s.isAnagram("anagram","nagaram")) #True
    print(s.isAnagram("rat","cat")) #False
    print(s.isAnagram("cat","cata")) #False
