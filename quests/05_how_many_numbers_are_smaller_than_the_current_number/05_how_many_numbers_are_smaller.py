from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n_freq = {} #store frequency of each num
        for i in nums:
            if i in n_freq:
                n_freq[i] +=1 #increase freq
            else:
                n_freq[i]=1

        sorted_keys = sorted(n_freq.keys())
        d_smaller_num_than_current ={}
        count = 0
        for i in sorted_keys:
            d_smaller_num_than_current[i]=count
            count += n_freq[i]

        l_smaller_num_than_current = []
        for i in nums:
            l_smaller_num_than_current += [d_smaller_num_than_current[i]]

        return l_smaller_num_than_current ,d_smaller_num_than_current

if __name__ == "__main__":        
    s = Solution()

    print(s.smallerNumbersThanCurrent([8,1,2,2,3]))