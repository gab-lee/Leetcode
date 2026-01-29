from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        apporach 1:
        dict = {sorted str: [list of str]}
        iterate through the list
        sort each str and check if it is in dict
        """
        d = {}
        for s in strs:
            temp = "".join(sorted(s))
            if temp not in d:
                d[temp] =[s]
            else:
                d[temp].append(s)
    
        return list(d.values())
if __name__ == "__main__":
    s = Solution()

    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) #[["bat"],["nat","tan"],["ate","eat","tea"]]
    print(s.groupAnagrams([""])) #[[""]]
    print(s.groupAnagrams(["a"])) #[["a"]]
