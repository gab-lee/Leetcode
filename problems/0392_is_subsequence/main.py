class Solution:
    def search_ch_in_string(self,ch,t,pos) -> int:
        for i in range(pos, len(t)):
            #print(ch,a)
            if t[i] == ch:
                return i + 1 #return positional value exlcude current num 
        return -1 #not found

    def isSubsequence(self, s: str, t: str) -> bool:
        #remove edge case
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        
        #iterate 
        pos = 0 
        for ch in s:
            #print(f"character:{ch}, pos:{pos}")
            pos = self.search_ch_in_string(ch,t,pos)
            if pos == -1: return False 
            else: continue
        
        return True     
        
if __name__ == "__main__":
    s = Solution()

    print(s.isSubsequence("abc","")) #Expect False
    print(s.isSubsequence("abc","ahbgdc")) #Expect True
    print(s.isSubsequence("axc","ahbgdc")) #Expect False