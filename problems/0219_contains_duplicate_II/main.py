class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        seen = []
        #edge cases
        if l <= 1 or k ==0:
            return False

        #create a sliding seen window 
        for i in range(k):
            if i +1  >= l:
                k = i+1
                break
            else:
                seen.append(nums[i+1])
    
        for i,n in enumerate(nums):
            if not seen:
                return False
            elif n in seen:
                return True
            elif i+k+1 >= l:
                seen.pop(0)
                continue
            else:
                seen.pop(0)
                seen.append(nums[i+k+1])

if __name__ == "__main__":
    s = Solution()

    print(s.containsNearbyDuplicate([1,2,3,1],3))#True
    print(s.containsNearbyDuplicate([1,0,1,1],1))#True
    print(s.containsNearbyDuplicate([1,2,3,1,2,3],2))#False
    print(s.containsNearbyDuplicate([99,99],2))#True
    print(s.containsNearbyDuplicate([1,2,3,4,5,6,7,8,9,9],3))#True
    print(s.containsNearbyDuplicate([1,2,3,1,2,3],2))#True