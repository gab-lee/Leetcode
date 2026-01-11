class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        
        #exclude empty matrix
        if not matrix or not matrix[0]:
            return False

        #Binary search insert 
        low, high = 0, m -1
        row = -1
        while low <= high:
            mid = (low + high)//2 
            if matrix[mid][0] <= target:
                row = mid 
                low = mid +1 #excludes mid 
            else:
                high = mid -1 #excludes mid

        if row == -1: #target out of range smaller than matrix[0][0]
            return False
        #matrix[row][0]< target < matrix[row+1][0] 
        if target > matrix[row][n-1]: #target does not exists in matrix 
            return False 

        print(f"row is {row}")
        #binary search within row 
        low, high =0, n-1
        while low <= high:
            mid = (low + high)//2 
            if matrix[row][mid] == target:
                return True 
            elif matrix[row][mid] < target:
                low = mid +1 #excludes mid 
            else:
                high = mid -1 #excludes mid
        
        return False 


if __name__ == "__main__":
    s = Solution()

    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))
    print(s.searchMatrix([[1]],1))
    print(s.searchMatrix([[1]],2))