class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        majority = len(nums)

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                if d[i] >= majority: 
                    return i #best case O(n/2), assume there is always a majority element
        return max(d, key=d.get)

if __name__ == "__main__":
    s = Solution()

    print(s.majorityElement([3,2,3])) #3
    print(s.majorityElement([2,2,1,1,1,2,2])) #2
    print(s.majorityElement([3,3,3,3,3,3,3,3,3,3,3,3,3])) #3