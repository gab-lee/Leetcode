class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #if n == 0:
        if m == 0:
            nums1[:n] = nums2
        else:
            nums1[:] = self.mergeLR(nums1[:m],nums2,m,n)
        print(nums1)

    def mergeLR(self,left,right,m,n):
        i = j = 0 
        out = []
        while i < len(left) and j < len(right):
            print(out)
            if left[i] <= right[j]:
                out.append(left[i])
                i += 1
            else: 
                out.append(right[j])
                j += 1
        
        out.extend(left[i:])
        out.extend(right[j:])
        return out 


if __name__ == "__main__":
    s = Solution()

    print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))
    print(s.merge([1],1,[],0))
    print(s.merge([0],0,[1],1))